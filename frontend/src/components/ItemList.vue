<template>
    <div v-if="items.loading">Chargement des articles...</div>
    <div v-else class="mt-10 space-y-12 sm:grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 lg:gap-12 lg:space-y-0">
        <div
            v-for="item in items.data"
            :key="item.name"
            class="card border-2 border-gray-200 rounded-lg flex overflow-hidden flex-col cursor-pointer hover:shadow-lg transition duration-300 ease-in-out hover:transform hover:scale-105"
            @click="openDialog(item)"
        >
            <div class="card-image w-full aspect-square">
                <img :src="item.image" :alt="item.name" class="w-full h-full object-cover" />
            </div>
            <div class="card-name p-4 bg-primary text-secondary text-center font-bold">{{ item.name }}</div>
        </div>
    </div>
    <Dialog v-model="productDialog">
        <template #body-title>
            <h2>{{ selectedItem.name }}</h2>
        </template>
        <template #body-content>
            <p>{{ selectedItem.description }}</p>
            <img :src="selectedItem.image" alt="selectedItem.name" class="w-full h-auto object-cover mt-4" />
        </template>
    </Dialog>
</template>

<script setup>
import { ref, watch } from 'vue'
import { createResource } from 'frappe-ui'
import { Dialog } from 'frappe-ui'

const productDialog = ref(false)
const selectedItem = ref({})

const props = defineProps({
    catalogid: String,
    universeid: String,
})

const parent_catalog = ref(props.catalogid)
const parent_universe = ref(props.universeid)

function openDialog(item) {
    selectedItem.value = item
    productDialog.value = true
}

const items = createResource({
    url: 'artyfetes_catalogs.api.get_items_of_universe',
    method: 'GET',
    fields: ['name', 'image', 'description'],
    params: { catalog_name: parent_catalog.value, universe_name: parent_universe.value },
})
items.fetch()
</script>