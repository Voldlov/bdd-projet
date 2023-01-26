<template>
  <EasyDataTable
      v-model:items-selected="itemsSelected"
    :headers="headers"
    :items="items"
  >
    <template #item-operation="item">
      <div class="operation-wrapper">
        <img
          src="./images/delete.png"
          class="operation-icon"
          @click="deleteItem(item)"
         alt="delete"/>
        <img
          src="./images/edit.png"
          class="operation-icon"
          @click="showModalEdit(item)"
         alt="edit"/>
      </div>
    </template>
  </EasyDataTable>
  <div></div>
  <div>
    <button>Créer</button>
    <button>Supprimer plusieurs</button>
  </div>
  <div v-show="modalEdit" class="form-edit-create">
    <h2>Edition</h2>
    <div>
      <p>Magnitude</p>
      <input v-model="editedItem.properties.mag"/>
    </div>
    <button @click="editItem">Valider</button>
  </div>

</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import type { Header, Item } from "vue3-easy-data-table";
import type {AxiosInstance} from 'axios';
import axios from 'axios';

const apiClient: AxiosInstance = axios.create({
  baseURL: "http://localhost:8080/",
  headers: {
    "Content-type": "application/json",
  },
});

export default defineComponent({

  data() {
    return {
      headers: [
        { text: "Magnitude", value: "properties.mag", sortable: true },
        { text: "Date", value: "weather_before.time", sortable: true },
        { text: "Longitute, Latitude, Profondeur", value: "geometry.coordinates"},
        { text: "Température avant (C)", value: "weather_before.temp_c", sortable: false },
        { text: "Température après (C)", value: "weather_after.temp_c", sortable: false },
        { text: "Pression avant (mb)", value: "weather_before.pressure_mb", sortable: false },
        { text: "Pression après (mb)", value: "weather_after.pressure_mb", sortable: false },
        { text: "Opérations", value: "operation", sortable: false },
        { text: "id", value: "id", sortable: false },
      ] as unknown as Header[],
    //   items:  [
    //   { "_id": "ObjectId(feweweoip)", "magnitude": 8, "date": "18-04-2012", "latitude": 245, "longitude": 142},
    // ] as Item[],
      // fetch items from api
      items: [] as Item[],
      itemsSelected: [] as Item[],
      modalEdit: false,
      editedItem: {properties: { mag: 0}, id: ""},
      newItem: {} as Item,
    };
  },

  mounted() {
    apiClient.get('/data').then((response) => {
      console.log(response.data);
      this.items = response.data;
    })
  },

  methods: {
    async deleteItem(item: Item) {
      apiClient.delete(`/data/${item.id}`).then((response) => {
        console.log(response.data);
        this.items = this.items.filter((i) => i.id !== item.id);
      })
      console.log("delete item", item);
    },
    addItem() {
      //await ApiService.post(this.newItem);
      this.items.push(this.newItem);
      this.newItem = {} as Item;
      console.log("add item", this.newItem);
    },
    showModalEdit(item: any) {
      this.modalEdit = true;
      this.editedItem = item
      console.log("show modal edit", this.items);
    },
    editItem() {
      //find and replace editeditem in items
      this.editedItem.properties.mag = Number(this.editedItem.properties.mag);
      const idx = this.items.findIndex((i) => i.id === this.editedItem.id);
      this.items.splice(idx, 1, this.editedItem);
      apiClient.put(`/data?id=${this.editedItem.id}`, this.editedItem).then((response) => {
        console.log(response.data);
      })
      //ApiService.update(this.editedItem._id, this.editedItem);
      this.cancelModalEdit();
    },
    cancelModalEdit() {
      this.modalEdit = false;
      this.editedItem = {properties: { mag: 0}, id: ""};
    },
  },
});
</script>

<style>
.operation-wrapper .operation-icon {
  width: 20px;
  cursor: pointer;
}

.form-edit-create {
  /* display in row */
  display: flex;
  flex-direction: column;
  /* align items in center */
  /* justify content in center */
}

.form-edit-create button {
  /* align self in center */
}
</style>
