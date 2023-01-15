<template>
    <div class="text-center mt-16 text-xl font-bold">
        <h2>{{ chronicle ? (chronicle as any).name : 'STDB'}}</h2>
    </div>
</template>

<script lang="ts" setup>
import { storeToRefs } from 'pinia';
import { useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();

const { chronicle } = storeToRefs(store);
</script>