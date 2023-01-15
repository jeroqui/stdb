<template>
    <div class="flex justify-between">
        <h1 class="text-4xl font-black">Chronicles</h1>
        <UIButton>New Chronicle</UIButton>
    </div>

    <div class="mt-8">
        <UIListItem
            v-for="item in result.chronicles"
            :key="item.id"
            @click="store.switchToChronicle(item.id)"
        >
            {{ item.name }}
        </UIListItem>
    </div>
</template>

<script lang="ts" setup>
import { useDashboardStore, boardNames } from '~~/stores/dashboardStore';

const store = useDashboardStore();

const query = gql`
query getChroncicles {
  chronicles {
    id,
    name
  }
}
`
const { result, error } = useQuery(query)

</script>