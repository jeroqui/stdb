<template>
    <div class="text-center mt-16 text-xl font-bold">
        <h2 v-if="chronicle">{{ (chronicle as any).name }}</h2>
        <UILogo v-else />
    </div>
</template>

<script lang="ts" setup>
import { storeToRefs } from 'pinia';
import { useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();

const { chronicle } = storeToRefs(store);
</script>