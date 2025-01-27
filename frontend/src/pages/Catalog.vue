<template>
    <h1>Univers de {{ current_catalog }}</h1>
    <UniverseList :catalogid="current_catalog" />
</template>

<script setup>
import { createResource } from 'frappe-ui'
import UniverseList from '../components/listings/UniverseList.vue'
import { useRoute } from 'vue-router'

const $route = useRoute()
const current_catalog = $route.params.catalogid
</script>