<template>
    <PartsPanel>
        <KeepAlive>
            <Suspense>
                <NuxtDynamic :isComponent="store.board.component"></NuxtDynamic>
    
                <template #fallback>
                    <div>
                        <SkeletonBoardDetail v-if="store.detail" />
                        <SkeletonBoardList v-else />
                    </div>
                </template>
            </Suspense>
        </KeepAlive>
    </PartsPanel>
</template>


<script setup>
import { useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();

const route = useRoute()

store.chronicle = route.params.slug[0]

definePageMeta({
    layout: "dashboard",
});

</script>