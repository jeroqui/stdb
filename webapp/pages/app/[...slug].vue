<template>
    <PartsPanel>
        <Suspense>
            <BoardsChronicleList v-if="store.board == boardNames.chroniclesList" />
            <BoardsCharacterList v-else-if="store.board == boardNames.charactersList" />
            <BoardsCharacterDetail
                v-else-if="store.board == boardNames.characterDetail"
                :detailId="$route.params.slug[1]"
            />
            <div v-else>{{ store.board }}</div>

            <template #fallback>
                <div>
                    <SkeletonBoardDetail v-if="store.detail" />
                    <SkeletonBoardList v-else />
                </div>
            </template>
        </Suspense>
    </PartsPanel>
</template>


<script setup>

import { boardNames, useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();

const route = useRoute()

store.chronicle = route.params.slug[0]

definePageMeta({
  layout: "dashboard",
});

</script>