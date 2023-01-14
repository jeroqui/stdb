<template>
    <div class="flex justify-between">
        <h1 class="text-4xl font-black">Chronicles</h1>
        <UIButton>New Chronicle</UIButton>
    </div>

    <div class="mt-8">
        <UIListItem v-for="item in ['Chronica 1', 'Nombre', 'Otra cosa']">{{item}}</UIListItem>
    </div>
</template>