Vue.config.devtools = true;

const app = new Vue({
  el: "#root",
  data: {
    first_editor: null,
    second_editor: null,
    running: false
  },
  computed: {
    get_starting_code() {
      return "class Main {\n\tmain ( ) : Int {\n\t\t0 ;\n\t} ;\n} ;\n";
    }
  },
  methods: {
    submit_code() {
      this.running = true;
      // eel.reset_app();
      eel.compile(this.first_editor.getValue())(response => {
        this.second_editor.setValue(response);
        this.running = false;
      });
    }
  },
  mounted() {
    this.first_editor = CodeMirror.fromTextArea(
      document.getElementById("form"),
      {
        lineNumbers: true,
        mode: "text/x-csrc"
      }
    );
    this.second_editor = CodeMirror.fromTextArea(
      document.getElementById("result"),
      {
        lineNumbers: false,
        mode: "text/x-csrc"
      }
    );
    this.first_editor.setSize(null, 550);
    this.first_editor.setValue(this.get_starting_code);
  }
});
