<template>
    <div class="relative">
        <div class="absolute z-10 left-0 right-0">
            <PartsMenuComponentsChronicle @click="switchTo(boardNames.chroniclesList)" />
        </div>
    
        <!-- Boards Menu -->
        <div class="absolute bg-black top-0 left-0 right-0 bottom-0 overflow-hidden" id="boards-menu" :class="store.detail ? 'detail' : ''">
            <div class="h-full flex flex-col justify-center">
                <div class="flex flex-col justify-around min-h-1/2">
                    <PartsMenuComponentsBoardButton @click="switchTo(boardNames.charactersList)">
                        Characters
                    </PartsMenuComponentsBoardButton>
                    <PartsMenuComponentsBoardButton @click="switchTo('locations')">
                        Locations
                    </PartsMenuComponentsBoardButton>
                    <PartsMenuComponentsBoardButton @click="switchTo('plots')">
                        Plots
                    </PartsMenuComponentsBoardButton>
                    <PartsMenuComponentsBoardButton @click="switchTo('sessions')">
                        Sessions
                    </PartsMenuComponentsBoardButton>
                </div>
            </div>
        </div>
    
        <!-- Items Menu -->
        <div class="flex flex-col mt-40 ml-16">
            <PartsMenuComponentsBoardItem v-for="item in ['item 1', 'other item', 'final item']">
                {{ item }}
            </PartsMenuComponentsBoardItem>
        </div>
    </div>
</template>


<style lang="scss" scoped>
#boards-menu {
    width: 100%;
    transition: width .4s ease;
    &.detail {
        width: 4rem;
    }
}
</style>

<script lang="ts" setup>
import { boardNames, useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();


function switchTo(detailName: string) {
    store.openBoard(detailName);
}


</script>