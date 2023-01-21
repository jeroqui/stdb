<template>
    <div class="my-10">
        <h2 class="text-2xl">Relationships</h2>

        <div>
            <div v-for="i in [1, 2, 3]"
                class="grid grid-cols-3"
            >
                <div>Character name</div>
                <div class="text-center">-- <i>loves</i> --></div>
                <div class="text-right">character {{ i }}</div>
            </div>
            <button>
                Add
            </button>
        </div>
    </div>
</template>