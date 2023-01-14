<template>
    <div class="bg-dark text-light min-h-screen grid grid-cols-4">
        <PartsMenu />
        <div class="col-span-3 flex flex-col">
            <div class="grow">
                <div class="flex justify-end p-2">
                    <UserProfileButon />
                </div>
                <slot />
            </div>
            <PartsFooter />
        </div>
    </div>
</template>