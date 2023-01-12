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
        />
        <img
          src="./images/edit.png"
          class="operation-icon"
          @click="editItem(item)"
        />
      </div>
    </template>
  </EasyDataTable>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import type { Header, Item } from "vue3-easy-data-table";
import ApiService from "@/services/api";

export default defineComponent({
  setup() {
    const headers: Header[] = [
      { text: "Name", value: "name" },
      { text: "Height (cm)", value: "height", sortable: true },
      { text: "Weight (kg)", value: "weight", sortable: true },
      { text: "Age", value: "age", sortable: true },
      { text: "Operation", value: "operation" },
    ];

    const items: Item[] = [
      { "name": "Curry", "height": 178, "weight": 77, "age": 20 },
      { "name": "James", "height": 180, "weight": 75, "age": 21 },
      { "name": "Jordan", "height": 181, "weight": 73, "age": 22 }
    ];

    const itemsSelected: Item[] = ref([]);

    const deleteItem = (item: Item) => {
      ApiService.delete(item._id);
      const idx = items.findIndex((i) => i._id === item._id);
      items.splice(idx, 1);
      console.log("delete item", item);
    };

    const editItem = (item: Item) => {
      //display edit form

      // update item data
      const idx = items.findIndex((i) => i._id === item._id);
      items.splice(idx, 1, item);

    };

    const update = (item: Item) => {
      ApiService.update(item._id, item);
      console.log("edit item", item);
    }

    return {
      headers,
      items,
      itemsSelected
    };
  },
});
</script>

<style>
.operation-wrapper .operation-icon {
  width: 20px;
  cursor: pointer;
}
</style>
