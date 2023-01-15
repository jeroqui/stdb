<template>
    <UIListItem>
        <div class="flex justify-between">
            <div>
                <b>
                    {{ name }}
                </b>
                Vampire
            </div>
            <div v-if="pc">
                PC
            </div>
        </div>
    </UIListItem>
</template>

<script lang="ts" setup>

const props = defineProps({
  name: {
    type: String,
    required: true
  },
  pc: {
    type: Boolean
  }
})


</script>