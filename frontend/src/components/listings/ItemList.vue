<template>
    <div v-if="items.loading">Chargement des articles...</div>
    <div v-else class="mt-10 space-y-12 sm:grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 lg:gap-12 lg:space-y-0">
        <div v-for="item in items.data" :key="item.name"
            class="card border-2 border-gray-200 rounded-lg flex overflow-hidden flex-col cursor-pointer hover:shadow-lg transition duration-300 ease-in-out hover:transform hover:scale-105"
            @click="openDialog(item)">
            <div class="card-image w-full aspect-square">
                <img :src="item.image" :alt="item.name" class="w-full h-full object-cover" />
            </div>
            <div class="card-name p-4 bg-primary text-secondary text-center font-bold">{{ item.name }}</div>
        </div>
    </div>
    <Dialog v-model="productDialog">
        <template #body-title class="text-center">
            <h2 class="text-2xl font-bold">{{ selectedItem.name }}</h2>
        </template>
        <template #body-content>
            <div class="grid grid-cols-2 gap-4">
                <div class="col-span-1">
                    <img :src="selectedItem.image || Placeholder" :alt="selectedItem.name"
                        class="w-full h-auto object-cover mt-4 max-w-80 block mx-auto" />
                    <div class="mt-8">
                        <h3>Catalogues liés :</h3>
                        <ul class="list-disc ml-4 mt-4">
                            <li v-for="(universes, catalogName) in catalogs.data" :key="catalogName" class="mb-4">
                                <!-- Catalog name at first level -->
                                <h4 class="font-bold text-lg">{{ catalogName }}</h4>
                                <!-- List of universes for this catalog -->
                                <ul class="ml-4 list-disc">
                                    <li v-for="universe in universes" :key="universe.title" class="text-gray-700">
                                        <span>{{ universe.title }}</span>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
                <span v-html="selectedItem.description"></span>
            </div>
        </template>
    </Dialog>
</template>

<script setup>
import { ref } from 'vue'
import { createResource, Dialog } from 'frappe-ui'
import Placeholder from '@/assets/imgs/placeholder.jpg'

const productDialog = ref(false)
const selectedItem = ref({})

const props = defineProps({
    catalogid: String,
    universeid: String,
})

const parent_catalog = ref(props.catalogid)
const parent_universe = ref(props.universeid)
const catalogs = ref({})

function openDialog(item) {
    selectedItem.value = item
    productDialog.value = true
    getItemCatalogs(item.name)
}

function getItemCatalogs(item_name) {
    catalogs.value = createResource({
        url: 'artyfetes_catalogs.api.get_active_catalogs',
        method: 'GET',
        fields: ['name'],
        params: { linked_item: item_name, only_visible: 1 },
    })
    catalogs.value.fetch()
}

const items = createResource({
    url: 'artyfetes_catalogs.api.get_items_of_universe',
    method: 'GET',
    fields: ['name', 'image', 'description'],
    params: { catalog_name: parent_catalog.value, universe_name: parent_universe.value },
})
items.fetch()
</script>