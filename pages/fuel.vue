<template>
  <div>
    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center overflow-hidden" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/products/test-product.jpg" 
          alt="Premium Fuel Services at Go For It Liquor"
          class="w-full h-full object-cover opacity-20"
          loading="eager"
          preload
        />
        <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(10, 10, 10, 0.95) 0%, rgba(26, 26, 26, 0.85) 50%, rgba(15, 15, 15, 0.95) 100%);"></div>
      </div>
      
      <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="mb-8">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
        </div>
        <h1 class="text-6xl md:text-8xl font-bold mb-8 leading-tight" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">
          Premium<br><span style="color: #D4AF37;">Fuel Services</span>
        </h1>
        <div class="w-32 h-1 mx-auto mb-8" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
        <p class="text-xl md:text-2xl mb-12 max-w-3xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
          Top-quality fuel at competitive prices, available 24/7.<br>
          <span style="color: #D4AF37;">Fresh fuel • Premium quality • Always available</span>
        </p>
        <div class="flex flex-col sm:flex-row gap-6 justify-center">
          <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              Get Directions
            </span>
          </a>
          <a href="tel:+16513952174" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
              </svg>
              Call Now
            </span>
          </a>
        </div>
      </div>
    </section>

    <!-- Current Fuel Prices -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-5xl md:text-6xl font-bold mb-8" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">Current Fuel Prices</h2>
          <p class="text-xl mb-6" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">Prices updated daily. Subject to change at station.</p>
          <div class="text-sm" style="color: #D4AF37; font-family: 'Inter', sans-serif;">
            Last Updated: {{ new Date().toLocaleString() }}
          </div>
        </div>

        <!-- Price Cards -->
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          <!-- Regular -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-500 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
            <div class="relative p-8 text-center">
              <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Regular</h3>
              <div class="text-4xl font-bold mb-2" style="color: #D4AF37; font-family: 'Inter', sans-serif;">$3.45</div>
              <p style="color: #B8B8B8; font-family: 'Inter', sans-serif;">per gallon</p>
            </div>
          </div>

          <!-- Plus -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-500 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
            <div class="relative p-8 text-center">
              <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Plus</h3>
              <div class="text-4xl font-bold mb-2" style="color: #D4AF37; font-family: 'Inter', sans-serif;">$3.65</div>
              <p style="color: #B8B8B8; font-family: 'Inter', sans-serif;">per gallon</p>
            </div>
          </div>

          <!-- Premium -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-500 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
            <div class="relative p-8 text-center">
              <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Premium</h3>
              <div class="text-4xl font-bold mb-2" style="color: #D4AF37; font-family: 'Inter', sans-serif;">$3.85</div>
              <p style="color: #B8B8B8; font-family: 'Inter', sans-serif;">per gallon</p>
            </div>
          </div>

          <!-- Diesel -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-500 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
            <div class="relative p-8 text-center">
              <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Diesel</h3>
              <div class="text-4xl font-bold mb-2" style="color: #D4AF37; font-family: 'Inter', sans-serif;">$3.95</div>
              <p style="color: #B8B8B8; font-family: 'Inter', sans-serif;">per gallon</p>
            </div>
          </div>
        </div>

        <!-- Important Notice -->
        <div class="relative overflow-hidden rounded-2xl shadow-2xl mb-16" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
          <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
          <div class="relative p-8">
            <div class="flex items-start">
              <svg class="w-8 h-8 mr-4 mt-1 transition-transform duration-300 hover:scale-110" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              <div>
                <h4 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Important Notice</h4>
                <p class="leading-relaxed" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                  Fuel prices are updated daily and may change throughout the day. 
                  Prices shown are for cash payments. Credit card payments may include additional fees. 
                  Please check current prices at the pump before fueling.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- CTA Buttons -->
        <div class="flex flex-col sm:flex-row gap-6 justify-center">
          <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              Get Directions
            </span>
          </a>
          <a href="tel:+16513952174" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
              </svg>
              Call Now
            </span>
          </a>
        </div>
      </div>
    </section>

    <!-- Quality Fuel Guarantee -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-5xl md:text-6xl font-bold mb-8" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">Quality Fuel Guarantee</h2>
          <p class="text-xl" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">Premium fuel quality you can trust</p>
        </div>
        <div class="grid md:grid-cols-3 gap-8">
          <div class="text-center group">
            <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
              <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Top Quality</h3>
            <p style="color: #B8B8B8; font-family: 'Inter', sans-serif;">We only sell premium quality fuel from trusted suppliers.</p>
          </div>
          
          <div class="text-center group">
            <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
              <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Fresh Daily</h3>
            <p style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Our tanks are refilled regularly to ensure fresh fuel.</p>
          </div>
          
          <div class="text-center group">
            <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
              <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">24/7 Access</h3>
            <p style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Gas pumps are available 24 hours a day, 7 days a week.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
useHead({
  title: 'Premium Fuel Services - Go For It Liquor',
  meta: [
    { name: 'description', content: 'Premium fuel services at Go For It Liquor. Competitive prices on regular, plus, premium, and diesel fuel. Quality fuel available 24/7 in East Bethel, MN.' },
    { name: 'keywords', content: 'premium fuel, gas prices, regular gas, premium gas, diesel, 24/7 fuel, East Bethel, Minnesota' }
  ]
})
</script>

<style scoped>
@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInRight {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.animate-fade-in-up {
  animation: fadeInUp 0.8s ease-out;
}

.animate-fade-in-left {
  animation: fadeInLeft 0.8s ease-out;
}

.animate-fade-in-right {
  animation: fadeInRight 0.8s ease-out;
}

.animate-delay-200 {
  animation-delay: 0.2s;
}

.animate-delay-400 {
  animation-delay: 0.4s;
}

.animate-delay-600 {
  animation-delay: 0.6s;
}

.animate-delay-800 {
  animation-delay: 0.8s;
}
</style>
