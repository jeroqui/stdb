<template>
    <div class="flex justify-center">
        <PartsMenuComponentsSideViewButton @click="store.openBoard(DashboardBoards.boardNames.CHARACTER_DETAIL, '')">
            <Icon name="ic:sharp-plus" size="1.5rem" />
        </PartsMenuComponentsSideViewButton>
        <PartsMenuComponentsSideViewButton>
            <Icon name="dashicons:admin-links" size="1.5rem"/>
        </PartsMenuComponentsSideViewButton>
    </div>

    <h3>Character Components:</h3>

    <BoardsCharacterList />
</template>

<script lang="ts" setup>
import { useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();

</script>