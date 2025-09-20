<template>
  <div>
    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center overflow-hidden" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/jack_daniel.png" 
          alt="Premium Spirits Collection at Go For It Liquor"
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
          Your Destination for<br><span style="color: #D4AF37;">Premium Spirits</span>
        </h1>
        <div class="w-32 h-1 mx-auto mb-8" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
        <p class="text-xl md:text-2xl mb-12 max-w-3xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
          Curated collection of the world's finest spirits, wines, and craft beverages.<br>
          <span style="color: #D4AF37;">Exclusive access • Expert guidance • Luxury at value</span>
        </p>
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

    <!-- Featured Brands Section -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-20">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-5xl md:text-6xl font-bold mb-8" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">Curated Collection</h2>
          <p class="text-xl max-w-4xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
            Hand-selected premium spirits from the world's most distinguished distilleries and wineries
          </p>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          

          <!-- Buffalo Trace -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.1);">
            <div class="p-8 text-center">
              <div class="mb-6">
                <NuxtImg 
                  src="/buffalo_trace_dark.png" 
                  alt="Buffalo Trace Kentucky Straight Bourbon Whiskey"
                  class="object-contain mx-auto drop-shadow-2xl transition-transform duration-500 group-hover:scale-110"
                  loading="lazy"
                />
              </div>
              <div class="mb-4">
                <div class="w-16 h-0.5 mx-auto mb-3" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Buffalo Trace</h3>
                <p class="text-sm" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Premium Bourbon</p>
              </div>
            </div>
          </div>

          <!-- Yellow Tail -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.1);">
            <div class="p-8 text-center">
              <div class="mb-6">
                <NuxtImg 
                  src="/tail_dark_1.png" 
                  alt="Yellow Tail Jammy Red Roo Wine"
                  class="object-contain mx-auto drop-shadow-2xl transition-transform duration-500 group-hover:scale-110"
                  loading="lazy"
                />
              </div>
              <div class="mb-4">
                <div class="w-16 h-0.5 mx-auto mb-3" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Yellow Tail</h3>
                <p class="text-sm" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Premium Wine</p>
              </div>
            </div>
          </div>

          <!-- Grey Goose -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.1);">
            <div class="p-8 text-center">
              <div class="mb-6">
                <div class="w-32 h-40 mx-auto flex items-center justify-center" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, rgba(212, 175, 55, 0.1) 100%); border-radius: 12px;">
                  <svg class="w-20 h-20 transition-transform duration-500 group-hover:scale-110" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                  </svg>
          </div>
        </div>
              <div class="mb-4">
                <div class="w-16 h-0.5 mx-auto mb-3" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Grey Goose</h3>
                <p class="text-sm mb-4" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Premium Vodka</p>
              </div>
              <p class="text-sm leading-relaxed mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                Crafted in France with the finest ingredients and traditional methods
              </p>
              <div class="text-xs space-y-1" style="color: #888888; font-family: 'Inter', sans-serif;">
                <p>• Original</p>
                <p>• La Poire</p>
                <p>• Le Citron</p>
      </div>
            </div>
          </div>
          
        </div>
      </div>
    </section>

    <!-- Exclusive Offers Section -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-20">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-5xl md:text-6xl font-bold mb-8" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">Exclusive Offers</h2>
          <p class="text-xl max-w-4xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
            Limited-time access to rare releases and exceptional value on premium selections
          </p>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
          <!-- Limited Release -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute top-6 right-6 z-10">
              <div class="relative">
                <div class="px-4 py-2 rounded-full text-sm font-semibold" style="background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); color: #0A0A0A; font-family: 'Inter', sans-serif;">
                  Limited Release
                </div>
                <div class="absolute -top-1 -right-1 w-3 h-3 rounded-full" style="background-color: #D4AF37; animation: pulse 2s infinite;"></div>
              </div>
            </div>
            <div class="p-8">
              <div class="mb-8">
                <NuxtImg 
                  src="/jack_daniel.png" 
                  alt="Jack Daniel's Limited Edition"
                  class="w-40 h-48 object-contain mx-auto drop-shadow-2xl transition-transform duration-500 group-hover:scale-110"
                />
              </div>
              <div class="text-center">
                <h3 class="text-2xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Jack Daniel's</h3>
                <p class="text-sm mb-4" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Single Barrel Select</p>
                <p class="text-sm leading-relaxed mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                  Hand-selected barrels for exceptional character and depth
                </p>
                <div class="flex items-center justify-center mb-8">
                  <span class="text-4xl font-bold mr-4" style="color: #D4AF37; font-family: 'Playfair Display', serif;">$89</span>
                  <span class="text-lg line-through" style="color: #888888; font-family: 'Inter', sans-serif;">$119</span>
          </div>
                <button class="w-full py-4 px-6 rounded-lg font-semibold transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 20px rgba(212, 175, 55, 0.3)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
                  Reserve Now
                </button>
              </div>
            </div>
          </div>
          
          <!-- Exclusive Access -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute top-6 right-6 z-10">
              <div class="relative">
                <div class="px-4 py-2 rounded-full text-sm font-semibold" style="background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); color: #0A0A0A; font-family: 'Inter', sans-serif;">
                  Exclusive Access
                </div>
                <div class="absolute -top-1 -right-1 w-3 h-3 rounded-full" style="background-color: #D4AF37; animation: pulse 2s infinite;"></div>
              </div>
            </div>
            <div class="p-8">
              <div class="mb-8">
                <div class="w-40 h-48 mx-auto flex items-center justify-center" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, rgba(212, 175, 55, 0.1) 100%); border-radius: 16px;">
                  <svg class="w-24 h-24 transition-transform duration-500 group-hover:scale-110" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                </svg>
                </div>
              </div>
              <div class="text-center">
                <h3 class="text-2xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Premium Wine</h3>
                <p class="text-sm mb-4" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Curated Selection</p>
                <p class="text-sm leading-relaxed mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                  Rare vintages and limited-production wines from renowned vineyards
                </p>
                <div class="flex items-center justify-center mb-8">
                  <span class="text-4xl font-bold mr-4" style="color: #D4AF37; font-family: 'Playfair Display', serif;">$45</span>
                  <span class="text-lg line-through" style="color: #888888; font-family: 'Inter', sans-serif;">$65</span>
                </div>
                <button class="w-full py-4 px-6 rounded-lg font-semibold transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 20px rgba(212, 175, 55, 0.3)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
                  Explore Collection
                </button>
              </div>
            </div>
          </div>
          
          <!-- Artisan Selection -->
          <div class="group relative overflow-hidden rounded-2xl transition-all duration-700 hover:scale-105" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute top-6 right-6 z-10">
              <div class="relative">
                <div class="px-4 py-2 rounded-full text-sm font-semibold" style="background: linear-gradient(135deg, #D4AF37 0%, #B8941F 100%); color: #0A0A0A; font-family: 'Inter', sans-serif;">
                  Artisan Selection
                </div>
                <div class="absolute -top-1 -right-1 w-3 h-3 rounded-full" style="background-color: #D4AF37; animation: pulse 2s infinite;"></div>
              </div>
            </div>
            <div class="p-8">
              <div class="mb-8">
                <div class="w-40 h-48 mx-auto flex items-center justify-center" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, rgba(212, 175, 55, 0.1) 100%); border-radius: 16px;">
                  <svg class="w-24 h-24 transition-transform duration-500 group-hover:scale-110" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
                </svg>
                </div>
              </div>
              <div class="text-center">
                <h3 class="text-2xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Craft Spirits</h3>
                <p class="text-sm mb-4" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Small Batch Collection</p>
                <p class="text-sm leading-relaxed mb-6" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                  Handcrafted spirits from master distillers and innovative craft producers
                </p>
                <div class="flex items-center justify-center mb-8">
                  <span class="text-4xl font-bold mr-4" style="color: #D4AF37; font-family: 'Playfair Display', serif;">$32</span>
                  <span class="text-lg line-through" style="color: #888888; font-family: 'Inter', sans-serif;">$48</span>
                </div>
                <button class="w-full py-4 px-6 rounded-lg font-semibold transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 20px rgba(212, 175, 55, 0.3)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
                  Discover More
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Why Choose Us Section -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-20">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-5xl md:text-6xl font-bold mb-8" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">The Premium Experience</h2>
          <p class="text-xl max-w-4xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
            Where exceptional spirits meet unparalleled expertise and exclusive access
          </p>
        </div>
        
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-12">
          <div class="text-center group">
            <div class="w-24 h-24 mx-auto mb-8 flex items-center justify-center transition-transform duration-500 group-hover:scale-110">
              <svg class="w-16 h-16" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Curated Collection</h3>
            <p class="leading-relaxed text-center" style="color: #B8B8B8; font-family: 'Inter', sans-serif; font-weight: 300;">Hand-selected premium spirits from the world's most distinguished distilleries and wineries</p>
          </div>
          
          <div class="text-center group">
            <div class="w-24 h-24 mx-auto mb-8 flex items-center justify-center transition-transform duration-500 group-hover:scale-110">
              <svg class="w-16 h-16" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"></path>
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Luxury at Value</h3>
            <p class="leading-relaxed text-center" style="color: #B8B8B8; font-family: 'Inter', sans-serif; font-weight: 300;">Exceptional quality and competitive pricing that makes premium spirits accessible</p>
          </div>
          
          <div class="text-center group">
            <div class="w-24 h-24 mx-auto mb-8 flex items-center justify-center transition-transform duration-500 group-hover:scale-110">
              <svg class="w-16 h-16" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1">
                <path stroke-linecap="round" stroke-linejoin="round" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Exclusive Access</h3>
            <p class="leading-relaxed text-center" style="color: #B8B8B8; font-family: 'Inter', sans-serif; font-weight: 300;">Limited releases, rare vintages, and exclusive bottles available only to our discerning clientele</p>
          </div>
          
          <div class="text-center group">
            <div class="w-24 h-24 mx-auto mb-8 flex items-center justify-center transition-transform duration-500 group-hover:scale-110">
              <svg class="w-16 h-16" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="1">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
              </svg>
            </div>
            <h3 class="text-2xl font-bold mb-6" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Expert Guidance</h3>
            <p class="leading-relaxed text-center" style="color: #B8B8B8; font-family: 'Inter', sans-serif; font-weight: 300;">Master sommeliers and spirits experts dedicated to helping you discover your perfect pour</p>
          </div>
        </div>

        <!-- Store Interior Image -->
        <div class="mt-16 text-center">
          <div class="relative max-w-4xl mx-auto">
            <NuxtImg 
              src="/test_image.jpg" 
              alt="Go For It Liquor Store Interior"
              class="w-full h-64 md:h-80 object-cover rounded-2xl shadow-2xl"
            />
            <div class="absolute inset-0 bg-gradient-to-t from-slate-900/50 to-transparent rounded-2xl"></div>
            <div class="absolute bottom-6 left-6 right-6 text-white">
              <h3 class="text-2xl font-bold mb-2">Visit Our Store</h3>
              <p class="text-slate-200">Experience our premium selection in person</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Visit Us Section -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-20">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-5xl md:text-6xl font-bold mb-8" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">Visit Our Sanctuary</h2>
          <p class="text-xl max-w-4xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
            Experience our curated collection in person at our East Bethel location
          </p>
        </div>
        
        <div class="grid lg:grid-cols-2 gap-12">
          <!-- Map -->
          <div class="relative overflow-hidden rounded-2xl shadow-2xl" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
            <div class="relative p-8">
              <div class="mb-6">
                <div class="w-16 h-0.5 mb-4" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h3 class="text-3xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Find Us</h3>
                <p class="text-sm" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Premium Spirits Destination</p>
              </div>
              <div class="relative overflow-hidden rounded-lg mb-8" style="border: 1px solid rgba(212, 175, 55, 0.3);">
                <iframe 
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2805.4882811108355!2d-93.18742019999999!3d45.318761599999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x52b31e8fd36cf5ef%3A0xb2626555f4804002!2sGo%20For%20It%20Gas!5e0!3m2!1sen!2sca!4v1758335989282!5m2!1sen!2sca" 
                  width="100%" 
                  height="320" 
                  style="border:0;" 
                  allowfullscreen="" 
                  loading="lazy" 
                  referrerpolicy="no-referrer-when-downgrade"
                ></iframe>
              </div>
              <a href="https://www.google.com/maps?cid=12853947706317488130" target="_blank" class="group inline-flex items-center px-8 py-4 rounded-lg font-semibold transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 20px rgba(212, 175, 55, 0.3)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
                <svg class="w-5 h-5 mr-3 transition-transform duration-300 group-hover:scale-110" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                </svg>
                Get Directions
              </a>
            </div>
          </div>
          
          <!-- Store Hours & Contact -->
          <div class="space-y-8">
            <div class="relative overflow-hidden rounded-2xl shadow-2xl" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
              <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
              <div class="relative p-8">
                <div class="mb-6">
                  <div class="w-16 h-0.5 mb-4" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                  <h3 class="text-3xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Store Hours</h3>
                  <p class="text-sm" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Always Open for Premium Service</p>
                </div>
                <div class="space-y-6">
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
                <div class="space-y-6">
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
        </div>
      </div>
    </section>

  </div>
</template>

<script setup>
// SEO Meta
useHead({
  title: 'Go For It Liquor - Your Local Liquor Destination',
  meta: [
    { name: 'description', content: 'Your premium liquor destination in East Bethel, MN. Wide selection of spirits, craft beer, and fine wine. Great prices, friendly service, and curated selection.' },
    { name: 'keywords', content: 'liquor store, spirits, whiskey, vodka, wine, beer, premium alcohol, East Bethel, Minnesota, Jack Daniels, craft beer' }
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
