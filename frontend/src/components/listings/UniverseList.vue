<template>
    <div v-if="universes.loading">Chargement des univers...</div>
    <div v-else class="mt-10 space-y-12 sm:grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 lg:gap-12 lg:space-y-0">
      <div v-for="universe in universes.data" :key="universe.name">
        <router-link :to="{ name: 'Universe', params: { universeid: universe.title }}" 
        class="bg-secondary text-primary text-center aspect-[10/12] text-2xl font-bold items-end justify-center flex
            hover:transform hover:scale-105 transition duration-300 ease-in-out shadow-[0_10px_10px_rgba(0,0,0,0.25)]
            hover:shadow-[3px_35px_35px_rgba(0,0,0,0.25)] rounded-lg overflow-hidden">
          <span class="flex justify-center items-center p-8 bg-primary text-secondary w-full">{{ universe.title }}</span>
        </router-link>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { createListResource } from 'frappe-ui'

const props = defineProps({
    catalogid: String,
})

const parent_catalog = ref(props.catalogid)

const universes = createListResource({
    doctype: 'Catalogs',
    fields: ['title', 'name'],
    filters: [["isactive", "=", 1],["isvisible","=",1],["type","=","univers"], ["parent_catalogs","=",parent_catalog.value]],
    })
universes.fetch()
</script>