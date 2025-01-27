<template>
    <h1>Produits de l'univers {{ current_universe }}</h1>
    <ItemList :universeid="current_universe" :catalogid="current_catalog" />
</template>

<script setup>
import ItemList from '../components/listings/ItemList.vue'
import { useRoute } from 'vue-router'

const $route = useRoute()
const current_catalog = $route.params.catalogid
const current_universe = $route.params.universeid
</script>