<template>
    <div class="flex hover:bg-dark">
        <div class="w-16 shrink-0 grow-0">
            <div class="rounded-full flex justify-center">
                <slot name="icon"></slot>
            </div>
        </div>
        <slot></slot>
    </div>
</template>