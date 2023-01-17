<template>
    <div class="skeleton rounded-xl m-1" :style="'width: ' + width + '; height: ' + height">

    </div>
</template>

<style lang="scss" scoped>
.skeleton {
  $from: #f5f5f5;
  $to: scale-color($from, $lightness: -10%);
  
  background: linear-gradient(-90deg, #efefef22 0%, #fcfcfc22 50%, #efefef22 100%);
  background-size: 400% 400%;
  animation: pulse 1.2s ease-in-out infinite;
  
  @keyframes pulse {
    0% {
      background-position: 0% 0%
    }
    100% {
      background-position: -135% 0%
    }
  }
}
</style>

<script lang="ts" setup>

const width = ref("100%");
const height = ref("2rem")

</script>