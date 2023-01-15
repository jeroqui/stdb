<template>
    <div class="flex bg-black hover:bg-dark transition-colors">
        <div class="w-16 shrink-0 grow-0">
            <div class="rounded-full flex justify-center">
                <slot name="icon"></slot>
            </div>
        </div>
        <slot></slot>
    </div>
</template>