<template>
    <div v-if="catalogs.loading">Chargement des catalogues...</div>
    <div v-else class="mt-10 space-y-12 sm:grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 lg:gap-12 lg:space-y-0">
      <div v-for="catalog in catalogs.data" :key="catalog.name">
        <router-link :to="{ name: 'Catalog', params: { catalogid: catalog.title }}" 
        class="bg-secondary text-primary text-center aspect-[10/15] text-2xl font-bold items-center justify-center flex
            hover:transform hover:scale-105 transition duration-300 ease-in-out hover:shadow-[0_35px_35px_rgba(0,0,0,0.25)]">
          {{ catalog.title }}
        </router-link>
        </div>
    </div>
</template>

<script setup>
import { createResource } from 'frappe-ui'

const catalogs = createResource({
    method: 'GET',
    url: 'artyfetes_catalogs.api.get_catalogs',
    params: { isactive: 1, isvisible: 1, type: 'Catalog' },
})
catalogs.fetch()
</script>