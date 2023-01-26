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
      <input v-model="editedItem.magnitude"/>
    </div>
    <div>
      <p>Longitude</p>
      <input v-model="editedItem.longitude"/>
    </div>
    <div>
      <p>Latitude</p>
      <input v-model="editedItem.latitude"/>
    </div>
    <button @click="editItem">Valider</button>
  </div>

</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import type { Header, Item } from "vue3-easy-data-table";
import ApiService from "@/services/api";

export default defineComponent({

  data() {
    return {
      headers: [
        { text: "Magnitude", value: "magnitude", sortable: true },
        { text: "Date", value: "date", sortable: true },
        { text: "Latitude", value: "latitude"},
        { text: "Longitude", value: "longitude"},
        { text: "Opérations", value: "operation", sortable: false },
      ] as unknown as Header[],
      items:  [
      { "_id": "ObjectId(feweweoip)", "magnitude": 8, "date": "18-04-2012", "latitude": 245, "longitude": 142},
    ] as Item[],
      // fetch items from api
      // items: ApiService.getEarthquakes(),
      itemsSelected: [] as Item[],
      modalEdit: false,
      editedItem: {} as Item,
    };
  },
  methods: {
    async deleteItem(item: Item) {
      //await ApiService.delete(item._id);
      const idx = this.items.findIndex((i) => i._id === item._id);
      this.items.splice(idx, 1);
      console.log("delete item", item);
    },
    showModalEdit(item: Item) {
      this.modalEdit = true;
      this.editedItem = item
      console.log("show modal edit", this.items);
    },
    editItem() {
      //find and replace editeditem in items
      const idx = this.items.findIndex((i) => i._id === this.editedItem._id);
      this.items.splice(idx, 1, this.editedItem);
      //ApiService.update(this.editedItem._id, this.editedItem);
      this.cancelModalEdit();
    },
    cancelModalEdit() {
      this.modalEdit = false;
      this.editedItem = {} as Item;
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
