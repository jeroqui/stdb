<template>
    <div class="flex justify-between">
        <h1 class="text-4xl font-black">Characters</h1>
        <UIButton @click="store.openBoard('CHARACTER_DETAIL')">New Character</UIButton>
    </div>

    <div class="mt-8">
        <UIListItem v-for="item in ['Chronica 1', 'Nombre', 'Otra cosa']">{{item}}</UIListItem>
    </div>
</template>

<script lang="ts" setup>
import { useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();

</script>