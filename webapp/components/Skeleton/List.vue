<template>
    <div>
        <div class="flex mt-10 flex-col">
            <SkeletonBlock v-for="i in [1, 2, 3]" :key="i" />
        </div>
    </div>
</template>