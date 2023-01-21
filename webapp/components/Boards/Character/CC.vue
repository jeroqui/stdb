<template>
    <div>
        <div v-if="false" class="my-4">
            <slot></slot>
        </div>
        <div v-else class="flex my-4 py-1 border border-primary justify-center rounded-xl">
            {{ buttonCreateText }}
        </div>
    </div>
</template>


<script lang="ts" setup>

const props = defineProps({
    buttonCreateText: {
        type: String,
    }
});

</script>