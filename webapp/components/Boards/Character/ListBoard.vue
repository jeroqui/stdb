<template>
    <div class="flex justify-between">
        <h1 class="text-4xl font-black">Characters</h1>
        <UIButton @click="store.openBoard(DashboardBoards.boardNames.CHARACTER_DETAIL, '')">New Character</UIButton>
    </div>

    <Suspense>
        <BoardsCharacterList />

        <template #fallback>
            <SkeletonList />
        </template>
    </Suspense>
</template>

<script lang="ts" setup>
import { useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();
</script>