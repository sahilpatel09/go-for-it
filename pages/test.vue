<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center">
    <div class="bg-white p-8 rounded-lg shadow-lg max-w-md w-full">
      <h1 class="text-3xl font-bold text-primary-500 mb-4">TailwindCSS Test</h1>
      <p class="text-gray-600 mb-6">If you can see this styled properly, TailwindCSS is working!</p>
      
      <div class="space-y-4">
        <button class="btn-primary w-full">Primary Button</button>
        <button class="btn-secondary w-full">Secondary Button</button>
        <button class="btn-outline w-full">Outline Button</button>
      </div>
      
      <div class="mt-6 p-4 bg-accent-50 rounded-lg">
        <p class="text-accent-800 font-medium">Accent color test</p>
      </div>
    </div>
  </div>
</template>

<script setup>
useHead({
  title: 'TailwindCSS Test - Go For It Gas'
})
</script>
