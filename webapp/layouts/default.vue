
import { PartsNavbar } from '~~/.nuxt/components';

<template>
    <div class="bg-dark text-light min-h-screen flex flex-col">
        <PartsNavbar />
        <div class="my-10 text-black grow">
            <slot />
        </div>
        <PartsFooter />
    </div>
</template>