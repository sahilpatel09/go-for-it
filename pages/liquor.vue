<template>
  <div>
    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center overflow-hidden" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="absolute inset-0">
        <NuxtImg 
          src="/images/backgrounds/home-background.jpeg" 
          alt="Go For It Liquor Store - Premium Spirits Destination"
          class="w-full h-full object-cover opacity-25"
          loading="eager"
          preload
        />
        <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(10, 10, 10, 0.4) 0%, rgba(26, 26, 26, 0.3) 50%, rgba(15, 15, 15, 0.4) 100%);"></div>
      </div>
      
      <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <div class="mb-8">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
        </div>
        <h1 class="text-6xl md:text-8xl font-bold mb-8 leading-tight" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">
          Liquor Store in East Bethel<br><span style="color: #D4AF37;">Premium Spirits Collection</span>
        </h1>
        <div class="w-32 h-1 mx-auto mb-8" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
        <p class="text-xl md:text-2xl mb-12 max-w-3xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
          Curated selection of the world's finest spirits, wines, and craft beverages.<br>
          <span style="color: #D4AF37;">Exclusive brands • Expert curation • Premium quality</span>
        </p>
        
        
        <div class="flex flex-col sm:flex-row gap-6 justify-center">
          <a href="https://maps.app.goo.gl/H1gsh7KUfgrg6ek49" target="_blank" class="group px-10 py-4 text-lg font-semibold rounded-lg transition-all duration-500 border-2" style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;" onmouseover="this.style.backgroundColor='#D4AF37'; this.style.color='#0A0A0A'; this.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='#D4AF37'; this.style.boxShadow='none';">
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

    <!-- Premium Collection -->
    <section class="py-24" style="background: linear-gradient(135deg, #0A0A0A 0%, #1A1A1A 50%, #0F0F0F 100%);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        
        <!-- <div class="text-center mb-20">
          <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
          <h2 class="text-5xl md:text-6xl font-bold mb-8" style="color: #F5F5F5; font-family: 'Playfair Display', serif; letter-spacing: -0.02em;">Premium Collection</h2>
          <p class="text-xl max-w-4xl mx-auto leading-relaxed" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
            Hand-selected spirits, craft beers, and fine wines from the world's most prestigious distilleries and wineries
          </p>
        </div> -->

        <!-- Signature Collection -->
        <!-- <div class="mb-20">
          <div class="text-center mb-12">
            <div class="w-16 h-0.5 mx-auto mb-4" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
            <h3 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Signature Collection</h3>
            <p class="text-lg max-w-3xl mx-auto" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">
              Discover our carefully curated selection of premium spirits, featuring iconic brands and exceptional quality
            </p>
          </div> -->
          
          <!-- Featured Jack Daniel's Collection -->
          <!-- <div class="relative overflow-hidden rounded-2xl shadow-2xl mb-16" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
            <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
            <div class="relative p-12">
              <div class="text-center mb-12">
                <div class="w-16 h-0.5 mx-auto mb-4" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                <h4 class="text-3xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Jack Daniel's Collection</h4>
                <p class="text-lg" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Tennessee's finest whiskey, crafted with tradition and excellence</p>
            </div>
            
            <div class="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                <div class="group relative overflow-hidden rounded-xl transition-all duration-500 hover:scale-105" style="background: linear-gradient(145deg, #0F0F0F 0%, #1A1A1A 100%); border: 1px solid rgba(212, 175, 55, 0.1);">
                  <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.02) 0%, transparent 50%, rgba(212, 175, 55, 0.02) 100%);"></div>
                  <div class="relative p-8">
                <div class="flex items-center space-x-6">
                      <div class="relative">
                  <NuxtImg 
                    src="/images/brands/jack-daniel.png" 
                    alt="Jack Daniel's Old No. 7"
                          class="w-20 h-28 object-contain transition-transform duration-500 group-hover:scale-110"
                  />
                        <div class="absolute -top-2 -right-2 w-4 h-4 rounded-full" style="background-color: #D4AF37; animation: pulse 2s infinite;"></div>
                      </div>
                  <div class="flex-1">
                        <h5 class="font-bold text-xl mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Jack Daniel's Old No. 7</h5>
                        <p class="text-sm mb-4" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">The original Tennessee whiskey with a smooth, mellow taste</p>
                    <div class="flex items-center justify-between">
                          <span class="text-sm" style="color: #888888; font-family: 'Inter', sans-serif;">750ml</span>
                        </div>
                      </div>
                  </div>
                </div>
              </div>
              
                <div class="group relative overflow-hidden rounded-xl transition-all duration-500 hover:scale-105" style="background: linear-gradient(145deg, #0F0F0F 0%, #1A1A1A 100%); border: 1px solid rgba(212, 175, 55, 0.1);">
                  <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.02) 0%, transparent 50%, rgba(212, 175, 55, 0.02) 100%);"></div>
                  <div class="relative p-8">
                <div class="flex items-center space-x-6">
                      <div class="relative">
                  <NuxtImg 
                    src="/images/brands/jack-daniels.jpg" 
                    alt="Jack Daniel's Gentleman Jack"
                          class="w-20 h-28 object-contain transition-transform duration-500 group-hover:scale-110"
                  />
                        <div class="absolute -top-2 -right-2 w-4 h-4 rounded-full" style="background-color: #D4AF37; animation: pulse 2s infinite;"></div>
                      </div>
                  <div class="flex-1">
                        <h5 class="font-bold text-xl mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Jack Daniel's Gentleman Jack</h5>
                        <p class="text-sm mb-4" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Double-mellowed for exceptional smoothness and character</p>
                    <div class="flex items-center justify-between">
                          <span class="text-sm" style="color: #888888; font-family: 'Inter', sans-serif;">750ml</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div> -->

        <!-- Products Section with Sidebar -->
        <div class="flex flex-col lg:flex-row gap-8 mb-20">
          <!-- Filter Sidebar -->
          <div class="lg:w-1/4">
            <div class="sticky top-8">
              <div class="relative overflow-hidden rounded-2xl shadow-2xl" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
                <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
                <div class="relative p-6">
                  <div class="mb-6">
                    <div class="w-16 h-0.5 mb-4" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
                    <h3 class="text-2xl font-bold mb-2" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Filter Products</h3>
                    <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Browse by category</p>
        </div>

                  <!-- Category Filter -->
                  <div class="mb-6">
                    <h4 class="text-lg font-semibold mb-4" style="color: #D4AF37; font-family: 'Inter', sans-serif;">Category</h4>
                    <div class="space-y-2">
                      <label 
                        v-for="category in categories" 
                        :key="category"
                        class="flex items-center space-x-3 cursor-pointer group"
                      >
                        <input 
                          type="checkbox" 
                          :value="category" 
                          v-model="selectedCategories"
                          class="sr-only"
                        />
                        <div 
                          :class="[
                            'w-4 h-4 rounded border-2 transition-all duration-300',
                            selectedCategories.includes(category) 
                              ? 'border-[#D4AF37] bg-[#D4AF37]' 
                              : 'border-[#666666] group-hover:border-[#D4AF37]'
                          ]"
                        >
                          <div 
                            v-if="selectedCategories.includes(category)"
                            class="w-2 h-2 bg-[#0A0A0A] rounded-sm mx-auto mt-0.5"
                          ></div>
                </div>
                        <span 
                          :class="[
                            'text-sm transition-colors duration-300',
                            selectedCategories.includes(category) 
                              ? 'text-[#D4AF37] font-semibold' 
                              : 'text-[#B8B8B8] group-hover:text-[#E5E5E5]'
                          ]"
                          style="font-family: 'Inter', sans-serif;"
                        >
                          {{ category }} ({{ getProductCount(category) }})
                        </span>
                      </label>
            </div>

                    <!-- Select All / Clear All -->
                    <div class="mt-4 pt-4 border-t border-[#333333]">
                      <div class="flex gap-2">
                        <button 
                          @click="selectAllCategories"
                          class="text-xs px-3 py-1 rounded transition-all duration-300"
                          style="color: #D4AF37; border: 1px solid #D4AF37; background: transparent; font-family: 'Inter', sans-serif;"
                          @mouseover="$event.target.style.backgroundColor='#D4AF37'; $event.target.style.color='#0A0A0A';"
                          @mouseout="$event.target.style.backgroundColor='transparent'; $event.target.style.color='#D4AF37';"
                        >
                          Select All
                        </button>
                        <button 
                          @click="clearAllCategories"
                          class="text-xs px-3 py-1 rounded transition-all duration-300"
                          style="color: #B8B8B8; border: 1px solid #666666; background: transparent; font-family: 'Inter', sans-serif;"
                          @mouseover="$event.target.style.backgroundColor='#666666'; $event.target.style.color='#F5F5F5';"
                          @mouseout="$event.target.style.backgroundColor='transparent'; $event.target.style.color='#B8B8B8';"
                        >
                          Clear All
                        </button>
                </div>
              </div>
            </div>

                  <!-- Product Count Summary -->
                  <div class="pt-4 border-t border-[#333333]">
                    <div class="text-center">
                      <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">
                        Showing {{ displayedProducts.length }} of {{ getTotalProductCount() }} products
                      </p>
                      <p v-if="selectedCategories.length > 1" class="text-xs mt-1" style="color: #666666; font-family: 'Inter', sans-serif;">
                        {{ selectedCategories.length }} categories selected
                      </p>
              </div>
            </div>
              </div>
            </div>
          </div>
        </div>

          <!-- Main Products Content -->
          <div class="lg:w-3/4">
            <div class="mb-8">
              <div class="w-16 h-0.5 mb-4" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
              <h3 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">{{ getCollectionTitle() }}</h3>
              <p class="text-lg" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">{{ getCollectionDescription() }}</p>
            </div>

            <!-- Loading State -->
            <div v-if="loading" class="text-center py-12">
              <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2" style="border-color: #D4AF37;"></div>
              <p class="mt-4 text-lg" style="color: #E5E5E5; font-family: 'Inter', sans-serif;">Loading products...</p>
            </div>

            <!-- Products Grid -->
            <div v-else class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
              <div 
                v-for="product in displayedProducts" 
                :key="`${product.category}-${product.name}`"
                class="group relative overflow-hidden rounded-xl transition-all duration-500 hover:scale-105" 
                style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 1px solid rgba(212, 175, 55, 0.1);"
              >
              <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.02) 0%, transparent 50%, rgba(212, 175, 55, 0.02) 100%);"></div>
                <div class="relative p-4 text-center">
                  <div class="relative mb-3">
                <NuxtImg 
                      :src="product.image_url" 
                      :alt="product.name"
                      class="w-36 h-40 object-contain rounded-lg mx-auto transition-transform duration-500 group-hover:scale-110"
                      loading="lazy"
                />
                  <div class="absolute -top-1 -right-1 w-3 h-3 rounded-full" style="background-color: #D4AF37; animation: pulse 2s infinite;"></div>
              </div>
                  <h4 class="font-bold text-xs mb-2 leading-tight" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">{{ product.name }}</h4>
                  <div v-if="product.rating" class="flex items-center justify-center mb-1">
                    <div class="flex items-center">
                      <svg class="w-3 h-3 mr-1" style="color: #D4AF37;" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                      </svg>
                      <span class="text-xs font-semibold" style="color: #D4AF37; font-family: 'Inter', sans-serif;">{{ product.rating }}</span>
              </div>
            </div>
              </div>
              </div>
            </div>

            <!-- Load More Button -->
            <div v-if="hasMoreProducts" class="text-center mt-12">
              <button 
                @click="loadMoreProducts"
                class="px-8 py-3 text-lg font-semibold rounded-lg transition-all duration-500 border-2"
                style="border-color: #D4AF37; color: #D4AF37; background: transparent; font-family: 'Inter', sans-serif;"
                @mouseover="$event.target.style.backgroundColor='#D4AF37'; $event.target.style.color='#0A0A0A'; $event.target.style.boxShadow='0 0 30px rgba(212, 175, 55, 0.4)';"
                @mouseout="$event.target.style.backgroundColor='transparent'; $event.target.style.color='#D4AF37'; $event.target.style.boxShadow='none';"
              >
                Load More Products
              </button>
            </div>
          </div>
        </div>


        <!-- Why Choose Us -->
        <div class="relative overflow-hidden rounded-2xl shadow-2xl mb-20" style="background: linear-gradient(145deg, #1A1A1A 0%, #0F0F0F 100%); border: 2px solid rgba(212, 175, 55, 0.2);">
          <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.05) 0%, transparent 50%, rgba(212, 175, 55, 0.05) 100%);"></div>
          <div class="relative p-12">
            <div class="text-center mb-12">
              <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
              <h3 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Why Choose Us</h3>
              <p class="text-lg" style="color: #D4AF37; font-family: 'Inter', sans-serif; font-weight: 500;">Your Premium Spirits Destination</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
              <div class="text-center group">
                <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                  <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M5 13l4 4L19 7"></path>
                  </svg>
              </div>
                <h4 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Curated Selection</h4>
                <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Hand-picked premium brands</p>
              </div>

              <div class="text-center group">
                <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                  <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
            </div>
                <h4 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Convenient Hours</h4>
                <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Open daily 6 AM - 10 PM</p>
            </div>

              <div class="text-center group">
                <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                  <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
                  </svg>
              </div>
                <h4 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Competitive Prices</h4>
                <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Great value on premium spirits</p>
            </div>

              <div class="text-center group">
                <div class="w-20 h-20 mx-auto mb-6 flex items-center justify-center transition-transform duration-500 group-hover:scale-110" style="background: linear-gradient(135deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.2) 100%); border-radius: 50%;">
                  <svg class="w-10 h-10" style="color: #D4AF37;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                  </svg>
              </div>
                <h4 class="text-xl font-bold mb-3" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Local Convenience</h4>
                <p class="text-sm" style="color: #B8B8B8; font-family: 'Inter', sans-serif;">Right here in East Bethel</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Call to Action -->
        <div class="text-center">
          <div class="mb-8">
            <div class="w-24 h-1 mx-auto mb-6" style="background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);"></div>
            <h3 class="text-4xl font-bold mb-4" style="color: #F5F5F5; font-family: 'Playfair Display', serif;">Ready to Explore?</h3>
            <p class="text-xl mb-8" style="color: #E5E5E5; font-family: 'Inter', sans-serif; font-weight: 300;">Visit us today and discover your new favorite spirit</p>
          </div>
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
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'

// Reactive data
const loading = ref(true)
const selectedCategories = ref(['Vodka'])
const productsPerPage = ref(20)
const currentPage = ref(1)
const allProducts = ref({})

// Available categories
const categories = ref(['Vodka', 'Beer', 'Seltzer', 'Sparkling & Sweet', 'Wine', 'Gin', 'Rum', 'Whisky', 'Tequila', 'Brandy & Cognac', 'Snacks', 'Drinks & Mixes', 'Premium Liquor'])

// Computed properties
const displayedProducts = computed(() => {
  const allSelectedProducts = []
  selectedCategories.value.forEach(category => {
    const categoryProducts = allProducts.value[category] || []
    // Add category information to each product
    const productsWithCategory = categoryProducts.map(product => ({
      ...product,
      category: category
    }))
    allSelectedProducts.push(...productsWithCategory)
  })
  
  // Sort products by rating (highest to lowest)
  const sortedProducts = allSelectedProducts.sort((a, b) => {
    const ratingA = parseFloat(a.rating) || 0
    const ratingB = parseFloat(b.rating) || 0
    return ratingB - ratingA
  })
  
  const startIndex = 0
  const endIndex = currentPage.value * productsPerPage.value
  return sortedProducts.slice(startIndex, endIndex)
})

const hasMoreProducts = computed(() => {
  const allSelectedProducts = []
  selectedCategories.value.forEach(category => {
    const categoryProducts = allProducts.value[category] || []
    allSelectedProducts.push(...categoryProducts)
  })
  return displayedProducts.value.length < allSelectedProducts.length
})

// Methods
const loadProducts = async () => {
  loading.value = true
  try {
    const [vodkaData, beerData, seltzerData, sparklingData, wineData, ginData, rumData, whiskyData, tequilaData, brandyData, snacksData, drinksData, liquorData] = await Promise.all([
      $fetch('/data/vodka_data.json'),
      $fetch('/data/beer_data.json'),
      $fetch('/data/seltzer_data.json'),
      $fetch('/data/sparkling_and_sweet_data.json'),
      $fetch('/data/wine_data.json'),
      $fetch('/data/gin_data.json'),
      $fetch('/data/rum_data.json'),
      $fetch('/data/whisky_data.json'),
      $fetch('/data/tequila_data.json'),
      $fetch('/data/brandy_and_cognac_data.json'),
      $fetch('/data/snacks_data.json'),
      $fetch('/data/drinks_and_mixes_data.json'),
      $fetch('/data/premium_liquor_data.json')
    ])
    
    allProducts.value = {
      'Vodka': vodkaData.categories.Vodka.products,
      'Beer': beerData.categories.Beer.products,
      'Seltzer': seltzerData.categories.Seltzer.products,
      'Sparkling & Sweet': sparklingData.categories['Sparkling & Sweet'].products,
      'Wine': wineData.categories.Wine.products,
      'Gin': ginData.categories.Gin.products,
      'Rum': rumData.categories.Rum.products,
      'Whisky': whiskyData.categories.Whisky.products,
      'Tequila': tequilaData.categories.Tequila.products,
      'Brandy & Cognac': brandyData.categories['Brandy & Cognac'].products,
      'Snacks': snacksData.categories.Snacks.products,
      'Drinks & Mixes': drinksData.categories['Drinks & Mixes'].products,
      'Premium Liquor': liquorData.categories['Premium Liquor'].products
    }
  } catch (error) {
    console.error('Error loading products:', error)
  } finally {
    loading.value = false
  }
}

const getProductCount = (category) => {
  return allProducts.value[category]?.length || 0
}

const getTotalProductCount = () => {
  let total = 0
  selectedCategories.value.forEach(category => {
    total += getProductCount(category)
  })
  return total
}

const getCollectionTitle = () => {
  if (selectedCategories.value.length === 0) {
    return 'No Categories Selected'
  } else if (selectedCategories.value.length === 1) {
    return `${selectedCategories.value[0]} Collection`
  } else if (selectedCategories.value.length === categories.value.length) {
    return 'All Products Collection'
  } else {
    return 'Mixed Collection'
  }
}

const getCollectionDescription = () => {
  if (selectedCategories.value.length === 0) {
    return 'Please select a category to view products'
  } else if (selectedCategories.value.length === 1) {
    return `Hand-selected ${selectedCategories.value[0].toLowerCase()} from the world's finest producers`
  } else if (selectedCategories.value.length === categories.value.length) {
    return 'Complete selection of premium spirits, craft beers, and fine wines from the world\'s finest producers'
  } else {
    return `Curated selection from ${selectedCategories.value.length} categories: ${selectedCategories.value.join(', ')}`
  }
}

const selectAllCategories = () => {
  selectedCategories.value = [...categories.value]
}

const clearAllCategories = () => {
  selectedCategories.value = []
}

const loadMoreProducts = () => {
  currentPage.value += 1
}

// Watch for category changes
watch(selectedCategories, () => {
  currentPage.value = 1
}, { deep: true })

// Lifecycle
onMounted(() => {
  loadProducts()
})

useHead({
  title: 'Liquor Store East Bethel MN — Go For It Liquor | Whiskey, Vodka & More',
  meta: [
    { name: 'description', content: 'Find premium spirits, beer, and wine at Go For It Liquor in East Bethel. Open daily with great selections.' },
    { name: 'keywords', content: 'liquor store East Bethel MN, premium spirits, whiskey, vodka, rum, tequila, craft beer, fine wine, Jack Daniels, Minnesota liquor store' },
    { name: 'canonical', content: 'https://go-for-it-wheat.vercel.app/liquor' }
  ],
  link: [
    { rel: 'sitemap', href: '/sitemap.xml', type: 'application/xml' }
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
