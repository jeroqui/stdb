<template>
    <div>
        <div class="flex justify-between">
            blok
            block
        </div>

        <div class="flex">
            <div v-for="i in [1, 2, 3]" :key="i">{{ i }}</div>
        </div>
    </div>
</template>