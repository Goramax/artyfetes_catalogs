<template>
      <h1>Tous les catalogues</h1>
  <CatalogList />
</template>

<script setup>
import { ref } from 'vue'
import { Dialog } from 'frappe-ui'
import { createResource } from 'frappe-ui'
import { session } from '../data/session'
import CatalogList from '../components/listings/CatalogList.vue'

// const ping = createResource({
//   url: 'ping',
//   auto: true,
// })

// const showDialog = ref(false)
</script>
