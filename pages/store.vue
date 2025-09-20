<template>
  <div>
    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center overflow-hidden" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/test_image.jpg" 
          alt="Premium Convenience Experience at Go For It Liquor"
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
          Premium<br><span style="color: #D4AF37;">Convenience</span>
        </h1>
        <div class="w-32 h-1 mx-auto mb-8" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
        <p class="text-xl md:text-2xl mb-12 max-w-3xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
          Curated essentials, artisanal coffee, and gourmet selections.<br>
          <span style="color: #D4AF37;">Quality • Convenience • Excellence</span>
        </p>
        <div class="flex flex-col sm:flex-row gap-6 justify-center">
          <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
            <span class="flex items-center justify-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              Visit Our Store
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

    <!-- Curated Essentials Section -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-20">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-5xl md:text-6xl font-bold mb-8" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">Curated Essentials</h2>
          <p class="text-xl max-w-4xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
            Hand-selected premium products, artisanal coffee, and gourmet selections for the discerning customer
          </p>
        </div>

        <!-- Premium Categories -->
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mb-20">
          <!-- Artisanal Coffee -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.1);">
            <div class="absolute top-6 right-6 z-10">
              <div class="relative">
                <div class="px-4 py-2 rounded-full text-sm font-semibold" style="background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); color: #0A0A0A; font-family: 'Inter', sans-serif;">
                  Artisanal
                </div>
                <div class="absolute -top-1 -right-1 w-3 h-3 rounded-full" style="background-color: #D4AF37; animation: pulse 2s infinite;"></div>
              </div>
            </div>
            <div class="p-8">
              <div class="mb-6">
                <div class="w-32 h-32 mx-auto flex items-center justify-center" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, rgba(212, 175, 55, 0.1) 100%); border-radius: 12px;">
                  <svg class="w-20 h-20 transition-transform duration-500 group-hover:scale-110" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                  </svg>
                </div>
              </div>
              <div class="mb-4">
                <div class="w-16 h-0.5 mx-auto mb-3" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Artisanal Coffee</h3>
                <p class="text-sm mb-4" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Premium Blends</p>
              </div>
              <p class="text-sm leading-relaxed mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                Hand-roasted beans, specialty drinks, and expertly crafted beverages
              </p>
              <div class="text-xs space-y-1" style="color: #888888; font-family: 'Inter', sans-serif;">
                <p>• Single Origin Beans</p>
                <p>• Espresso Drinks</p>
                <p>• Cold Brew Selection</p>
              </div>
            </div>
          </div>

          <!-- Gourmet Food -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.1);">
            <div class="absolute top-6 right-6 z-10">
              <div class="relative">
                <div class="px-4 py-2 rounded-full text-sm font-semibold" style="background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); color: #0A0A0A; font-family: 'Inter', sans-serif;">
                  Gourmet
                </div>
                <div class="absolute -top-1 -right-1 w-3 h-3 rounded-full" style="background-color: #D4AF37; animation: pulse 2s infinite;"></div>
              </div>
            </div>
            <div class="p-8">
              <div class="mb-6">
                <div class="w-32 h-32 mx-auto flex items-center justify-center" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, rgba(212, 175, 55, 0.1) 100%); border-radius: 12px;">
                  <svg class="w-20 h-20 transition-transform duration-500 group-hover:scale-110" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                  </svg>
                </div>
              </div>
              <div class="mb-4">
                <div class="w-16 h-0.5 mx-auto mb-3" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Gourmet Food</h3>
                <p class="text-sm mb-4" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Fresh Daily</p>
              </div>
              <p class="text-sm leading-relaxed mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                Handcrafted sandwiches, artisanal pizzas, and chef-inspired selections
              </p>
              <div class="text-xs space-y-1" style="color: #888888; font-family: 'Inter', sans-serif;">
                <p>• Artisan Sandwiches</p>
                <p>• Wood-Fired Pizza</p>
                <p>• Chef Specials</p>
              </div>
            </div>
          </div>

          <!-- Premium Snacks -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.1);">
            <div class="absolute top-6 right-6 z-10">
              <div class="relative">
                <div class="px-4 py-2 rounded-full text-sm font-semibold" style="background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); color: #0A0A0A; font-family: 'Inter', sans-serif;">
                  Premium
                </div>
                <div class="absolute -top-1 -right-1 w-3 h-3 rounded-full" style="background-color: #D4AF37; animation: pulse 2s infinite;"></div>
              </div>
            </div>
            <div class="p-8">
              <div class="mb-6">
                <div class="w-32 h-32 mx-auto flex items-center justify-center" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, rgba(212, 175, 55, 0.1) 100%); border-radius: 12px;">
                  <svg class="w-20 h-20 transition-transform duration-500 group-hover:scale-110" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                  </svg>
                </div>
              </div>
              <div class="mb-4">
                <div class="w-16 h-0.5 mx-auto mb-3" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Premium Snacks</h3>
                <p class="text-sm mb-4" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Curated Selection</p>
              </div>
              <p class="text-sm leading-relaxed mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                Hand-selected gourmet snacks, organic options, and international treats
              </p>
              <div class="text-xs space-y-1" style="color: #888888; font-family: 'Inter', sans-serif;">
                <p>• Organic Options</p>
                <p>• International Treats</p>
                <p>• Artisan Chocolates</p>
              </div>
            </div>
          </div>

          <!-- Essential Services -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.1);">
            <div class="absolute top-6 right-6 z-10">
              <div class="relative">
                <div class="px-4 py-2 rounded-full text-sm font-semibold" style="background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); color: #0A0A0A; font-family: 'Inter', sans-serif;">
                  Services
                </div>
                <div class="absolute -top-1 -right-1 w-3 h-3 rounded-full" style="background-color: #D4AF37; animation: pulse 2s infinite;"></div>
              </div>
            </div>
            <div class="p-8">
              <div class="mb-6">
                <div class="w-32 h-32 mx-auto flex items-center justify-center" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, rgba(212, 175, 55, 0.1) 100%); border-radius: 12px;">
                  <svg class="w-20 h-20 transition-transform duration-500 group-hover:scale-110" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                  </svg>
                </div>
              </div>
              <div class="mb-4">
                <div class="w-16 h-0.5 mx-auto mb-3" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Essential Services</h3>
                <p class="text-sm mb-4" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Complete Convenience</p>
              </div>
              <p class="text-sm leading-relaxed mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                Premium tobacco, lottery services, and essential convenience items
              </p>
              <div class="text-xs space-y-1" style="color: #888888; font-family: 'Inter', sans-serif;">
                <p>• Premium Tobacco</p>
                <p>• Lottery Services</p>
                <p>• Essential Items</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Signature Experience -->
        <div class="relative overflow-hidden rounded-2xl shadow-2xl" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
          <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
          <div class="relative p-12">
            <div class="text-center mb-12">
              <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
              <h3 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Signature Experience</h3>
              <p class="text-lg" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Where Premium Meets Convenience</p>
            </div>
            <div class="grid md:grid-cols-3 gap-8">
              <div class="text-center group">
                <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                  <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                </svg>
              </div>
                <h4 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Artisanal Coffee</h4>
                <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Hand-roasted beans and expertly crafted beverages</p>
            </div>
            
              <div class="text-center group">
                <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                  <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                </svg>
              </div>
                <h4 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Gourmet Food</h4>
                <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Chef-inspired selections made fresh daily</p>
            </div>
            
              <div class="text-center group">
                <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                  <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                </svg>
                </div>
                <h4 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Premium Selection</h4>
                <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Curated products for the discerning customer</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Visit Our Store -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="mb-12">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-5xl md:text-6xl font-bold mb-8" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">Visit Our Store</h2>
          <p class="text-xl max-w-3xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
            Experience premium convenience in person at our East Bethel location
          </p>
        </div>
        
        <div class="grid md:grid-cols-2 gap-8 mb-12">
          <div class="relative overflow-hidden rounded-2xl shadow-2xl" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
            <div class="relative p-8">
              <div class="mb-6">
                <div class="w-16 h-0.5 mb-4" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-3xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Store Hours</h3>
                <p class="text-sm" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Always Open for Premium Service</p>
              </div>
              <div class="space-y-4">
                <div class="flex justify-between items-center py-3 border-b" style="border-color: rgba(212, 175, 55, 0.2);">
                  <span class="font-semibold" style="color: #D4AF37; font-family: 'Inter', sans-serif;">Monday - Sunday</span>
                  <span style="color: #F5F5F5; font-family: 'Inter', sans-serif;">6:00 AM - 10:00 PM</span>
                </div>
                <div class="flex justify-between items-center py-3">
                  <span class="font-semibold" style="color: #D4AF37; font-family: 'Inter', sans-serif;">Gas Pumps</span>
                  <span style="color: #F5F5F5; font-family: 'Inter', sans-serif;">24/7 Available</span>
              </div>
              </div>
            </div>
          </div>
          
          <div class="relative overflow-hidden rounded-2xl shadow-2xl" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
            <div class="relative p-8">
              <div class="mb-6">
                <div class="w-16 h-0.5 mb-4" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-3xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Contact Information</h3>
                <p class="text-sm" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Connect With Our Experts</p>
              </div>
              <div class="space-y-4">
                <div class="flex items-center py-3 border-b" style="border-color: rgba(212, 175, 55, 0.2);">
                  <svg class="w-6 h-6 mr-4 transition-transform duration-300 hover:scale-110" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
                  <span style="color: #F5F5F5; font-family: 'Inter', sans-serif;">3255 Viking Blvd NE, East Bethel, MN 55092</span>
              </div>
                <div class="flex items-center py-3">
                  <svg class="w-6 h-6 mr-4 transition-transform duration-300 hover:scale-110" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                </svg>
                  <a href="tel:+16513952174" class="transition-colors duration-300 hover:opacity-80" style="color: #F5F5F5; font-family: 'Inter', sans-serif;">(651) 395-2174</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="flex flex-col sm:flex-row gap-6 justify-center">
          <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
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
  </div>
</template>

<script setup>
useHead({
  title: 'Premium Convenience Store - Go For It Liquor',
  meta: [
    { name: 'description', content: 'Experience premium convenience with artisanal coffee, gourmet food, curated snacks, and essential services. Premium quality with exceptional service in East Bethel, MN.' },
    { name: 'keywords', content: 'premium convenience store, artisanal coffee, gourmet food, curated snacks, essential services, East Bethel, Minnesota' }
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
