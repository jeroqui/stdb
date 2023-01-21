<template>
    <div>
        <div class="min-h-screen" v-if="store.board.is_fullscreen">
            <NuxtDynamic :isComponent="store.board.component"></NuxtDynamic>
        </div>
        <PartsPanel v-else>
            <!-- Panel Boards ~switch statement~ -->
            <KeepAlive>
                <BoardsChronicleList v-if="store.board.name === DashboardBoards.boardNames.CHRONICLES_LIST" />
                <BoardsCharacterListBoard v-else-if="store.board.name === DashboardBoards.boardNames.CHARACTERS_LIST" />
                <BoardsCharacterDetail v-else-if="store.board.name === DashboardBoards.boardNames.CHARACTER_DETAIL" :detailId="detailId" :key="detailId" />
            </KeepAlive>
        </PartsPanel>
    </div>
</template>


<script setup>
import { storeToRefs } from 'pinia';
import { useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();
const { detailId } = storeToRefs(store);

const route = useRoute()

store.chronicle = route.params.slug[0]

definePageMeta({
    layout: "dashboard",
});

</script>