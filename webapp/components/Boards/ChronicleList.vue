<template>
    <div class="flex justify-between">
        <h1 class="text-4xl font-black">Chronicles</h1>
        <UIButton>New Chronicle</UIButton>
    </div>

    <div class="mt-8">
        <UIListItem
            v-for="item in data?.chronicles"
            :key="item.id"
            >
            <NuxtLink
                :to="'/app/'+item.id"
            >
                {{ item.name }}
            </NuxtLink>
        </UIListItem>
    </div>
</template>

<script lang="ts" setup>
import { useDashboardStore } from '~~/stores/dashboardStore';

const store = useDashboardStore();

const query = gql`
query getChroncicles {
  chronicles {
    id,
    name
  }
}
`
type ChroniclesResult = {
    chronicles: {
        id: string;
        name: string;
    }[]
}

const { data, error } = await useAsyncQuery<ChroniclesResult>(query)

</script>