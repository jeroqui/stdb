<template>
    <div>
        <div class="min-h-screen" v-if="store.board.is_fullscreen">
            <NuxtDynamic :isComponent="store.board.component"></NuxtDynamic>
        </div>
        <PartsPanel v-else>
            <KeepAlive>
                <NuxtDynamic :isComponent="store.board.component"></NuxtDynamic>
            </KeepAlive>
        </PartsPanel>
    </div>
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