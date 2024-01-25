<template>
  <q-page class="row items-center justify-evenly">
    <example-component
      title="Example component"
      active
      :todos="todos"
      :meta="meta"
    ></example-component>
    <q-uploader
        url="http://127.0.0.1:5000/upload"
        label="Sube la foto del diagrama E/R"
        accept="image/*"
        square
        flat
        bordered
        style="max-width: 300px"
      />
  </q-page>
</template>

<script lang="ts">
import ExampleComponent from 'components/ExampleComponent.vue';
import { defineComponent, ref } from 'vue';
import { api } from 'src/boot/axios';
export default defineComponent({
  name: 'IndexPage',
  components: { ExampleComponent },
  setup () {
    const todos = ref<[]>([]);
    return { todos };
  },
  mounted() {
    this.getFromApi();
  }, 
  methods: {
    getFromApi() {
      api.get('/returnjson').then(res => {
        this.todos = res.data;
      })
    }
  }
});
</script>
