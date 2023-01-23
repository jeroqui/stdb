<template>
    <div
        v-if="!editing"
        tabindex="0"
        @focus="edit()"
        @click="edit()"
        class="w-full cursor-text"
    >
        <span v-if="text">{{ text }}</span>
        <span v-else class="text-dark text-opacity-60">{{ defaultText }}</span>
    </div>
    <input
        v-else
        class="w-full bg-light placeholder:text-dark placeholder:text-opacity-60"
        type="text" 
        :placeholder="defaultText"
        :value="text || ''"
        ref="editInput"
        @blur="blur()"
    >
</template>

<script lang="ts" setup>

const props = defineProps({
    text: {
        type: String,
    },
    defaultText: {
        type: String,
        required: true,
    }
})

const editing = ref(false);
const editInput = ref<HTMLElement>();

async function edit() {
    editing.value = true;

    await nextTick();

    if (editInput.value) {
        editInput.value.focus();
    }
}

function blur(){
    editing.value = false;
}

</script>