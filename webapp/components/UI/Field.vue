<template>
    <div
        v-if="!editing"
        tabindex="0"
        @focus="edit()"
        @click="edit()"
        class="w-full cursor-text"
    >
        <span v-if="text">{{ local_text }}</span>
        <span v-else class="text-dark text-opacity-60">{{ defaultText }}</span>
    </div>
    <input
        v-else
        class="w-full bg-light placeholder:text-dark placeholder:text-opacity-60"
        type="text" 
        :placeholder="defaultText"
        v-model="local_text"
        ref="editInput"
        @keyup.enter="editInput?.blur()"
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

const emit = defineEmits<{
    (e: 'change', value: string): void
}>()


const editing = ref(false);
const editInput = ref<HTMLElement>();
const local_text = ref(props.text);

async function edit() {
    editing.value = true;

    await nextTick();

    if (editInput.value) {
        editInput.value.focus();
    }
}

function blur(){
    editing.value = false;
    if (props.text != local_text.value) {
        emit("change", local_text.value || '')
    }
}

</script>