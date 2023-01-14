<template>
    <div class="relative">
        <div class="absolute z-10 left-0 right-0">
            <PartsMenuComponentsChronicle />
        </div>
    
        <!-- Boards Menu -->
        <div class="absolute bg-black top-0 left-0 right-0 bottom-0 overflow-hidden" id="boards-menu">
            <div class="h-full flex flex-col justify-center">
                <div class="flex flex-col justify-around min-h-1/2">
                    <PartsMenuComponentsBoardButton>
                        Characters
                    </PartsMenuComponentsBoardButton>
                    <PartsMenuComponentsBoardButton>
                        Locations
                    </PartsMenuComponentsBoardButton>
                    <PartsMenuComponentsBoardButton>
                        Plots
                    </PartsMenuComponentsBoardButton>
                    <PartsMenuComponentsBoardButton>
                        Sessions
                    </PartsMenuComponentsBoardButton>
                </div>
            </div>
        </div>
    
        <!-- Items Menu -->
        <div class="min-h-full flex flex-col justify-center ml-16">
            <PartsMenuComponentsBoardItem v-for="item in ['item 1', 'other item', 'final item']">
                {{ item }}
            </PartsMenuComponentsBoardItem>
        </div>
    </div>
</template>


<style scoped>
#boards-menu {
    width: 4rem;
}
</style>