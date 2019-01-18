<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>todos</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.Todo-modal>Add Todo</button>
        <br><br>

        <!-- todos table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Todo</th>
              <th scope="col">assignee</th>
              <th scope="col">Done?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(Todo, index) in todos" :key="index">
              <td>{{ Todo.todo }}</td>
              <td>{{ Todo.assignee }}</td>
              <td>
                <span v-if="Todo.done">Yes</span>
                <span v-else>No</span>
              </td>
              <td>${{ Todo.price }}</td>
              <td>
                <button type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.Todo-update-modal
                        @click="editTodo(Todo)">
                    Update
                </button>
                <button type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeleteTodo(Todo)">
                    Delete
                </button>
                <router-link :to="`/order/${Todo.id}`"
                             class="btn btn-primary btn-sm">
                    Purchase
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>

    <!-- add Todo modal -->
    <b-modal ref="addTodoModal"
             id="Todo-modal"
            title="Add a new Todo"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group"
                      label="Title:"
                      label-for="form-title-input">
            <b-form-input id="form-title-input"
                          type="text"
                          v-model="addTodoForm.todo"
                          required
                          placeholder="Enter title">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        v-model="addTodoForm.assignee"
                        required
                        placeholder="Enter author">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
            <b-form-checkbox-group v-model="addTodoForm.done" id="form-checks">
              <b-form-checkbox value="true">Done?</b-form-checkbox>
            </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal ref="editTodoModal"
             id="Todo-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-edit-group"
                      label="Title:"
                      label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.todo"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
          <b-form-input id="form-author-edit-input"
                        type="text"
                        v-model="editForm.assignee"
                        required
                        placeholder="Enter author">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.done" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      todos: [],
      addTodoForm: {
        todo: '',
        assignee: '',
        done: [],
      },
      editForm: {
        id: '',
        todo: '',
        assignee: '',
        done: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    gettodos() {
      const path = 'http://localhost:5000/todos';
      axios.get(path)
        .then((res) => {
          this.todos = res.data.todos;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTodo(payload) {
      const path = 'http://localhost:5000/todos';
      axios.post(path, payload)
        .then(() => {
          this.gettodos();
          this.message = 'Todo added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.gettodos();
        });
    },
    updateTodo(payload, TodoID) {
      const path = `http://localhost:5000/todos/${TodoID}`;
      axios.put(path, payload)
        .then(() => {
          this.gettodos();
          this.message = 'Todo updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.gettodos();
        });
    },
    removeTodo(TodoID) {
      const path = `http://localhost:5000/todos/${TodoID}`;
      axios.delete(path)
        .then(() => {
          this.gettodos();
          this.message = 'Todo removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.gettodos();
        });
    },
    initForm() {
      this.addTodoForm.todo = '';
      this.addTodoForm.assignee = '';
      this.addTodoForm.done = [];
      this.editForm.id = '';
      this.editForm.todo = '';
      this.editForm.assignee = '';
      this.editForm.done = [];
      this.editForm.id = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTodoModal.hide();
      let read = false;
      if (this.addTodoForm.read[0]) read = true;
      const payload = {
        todo: this.addTodoForm.title,
        assignee: this.addTodoForm.author,
        done, // property shorthand
      };
      this.addTodo(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTodoModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        todo: this.editForm.title,
        assignee: this.editForm.author,
        done, // property shorthand
      };
      this.updateTodo(payload, this.editForm.id);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTodoModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTodoModal.hide();
      this.initForm();
      this.gettodos(); // why?
    },
    onDeleteTodo(Todo) {
      this.removeTodo(Todo.id);
    },
    editTodo(Todo) {
      this.editForm = Todo;
    },
  },
  created() {
    this.gettodos();
  },
};
</script>
