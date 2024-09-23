> allianz_coords <- c(-46.67835891788951, -23.527374755405372)
> morumbi_coords <- c(-46.72005013426793, -23.600781655693297)
> allianz_coords <- c(-46.67835891788951, -23.527374755405372)
> morumbi_coords <- c(-46.72005013426793, -23.600781655693297)
> maracana_coords <- c(-43.230166, -22.912166)  # Rio de Janeiro
> mineirao_coords <- c(-43.971249, -19.865915)  # Belo Horizonte
> arena_grêmio_coords <- c(-51.184061, -29.973086)  # Porto Alegre
> arena_corinthians_coords <- c(-46.474737, -23.545117)  # São Paulo
> arena_da_baixada_coords <- c(-49.276640, -25.450356)  # Curitiba
> castelao_coords <- c(-38.522332, -3.732762)  # Fortaleza
> beira_rio_coords <- c(-51.227006, -30.064436)  # Porto Alegre
> mane_garrincha_coords <- c(-47.899503, -15.780103)  # Brasília

library(leaflet)
leaflet() %>% 
  
+ addTiles() %>% 
+ addMarkers(lng = morumbi_coords[1], lat = morumbi_coords[2], popup = "Morumbi - Estádio do Tetra Campeão Da Libertadores 2024 - SPFC - Tri-Campeão Mundial - 92-93-05") %>%
+ addMarkers(lng = allianz_coords[1], lat = allianz_coords[2], popup = "Allianz Parque - O Estádio alugado do time que ainda busca o mundial") %>%
+ addMarkers(lng = maracana_coords[1], lat = maracana_coords[2], popup = "Maracanã - Estádio icônico no Rio de Janeiro") %>%
+ addMarkers(lng = mineirao_coords[1], lat = mineirao_coords[2], popup = "Mineirão - Estádio em Belo Horizonte") %>%
+ addMarkers(lng = arena_grêmio_coords[1], lat = arena_grêmio_coords[2], popup = "Arena do Grêmio - Porto Alegre") %>%
+ addMarkers(lng = arena_corinthians_coords[1], lat = arena_corinthians_coords[2], popup = "Arena Corinthians - São Paulo") %>%
+ addMarkers(lng = arena_da_baixada_coords[1], lat = arena_da_baixada_coords[2], popup = "Arena da Baixada - Curitiba") %>%
+ addMarkers(lng = castelao_coords[1], lat = castelao_coords[2], popup = "Castelão - Fortaleza") %>%
+ addMarkers(lng = beira_rio_coords[1], lat = beira_rio_coords[2], popup = "Beira-Rio - Porto Alegre") %>%
+ addMarkers(lng = mane_garrincha_coords[1], lat = mane_garrincha_coords[2], popup = "Mané Garrincha - Brasília") %>% 

+ addPolylines(lng = c(morumbi_coords[1], allianz_coords[1]), lat = c(morumbi_coords[2], allianz_coords[2]), color = "blue") %>%
+ addPolylines(lng = c(morumbi_coords[1], maracana_coords[1]), lat = c(morumbi_coords[2], maracana_coords[2]), color = "yellow") %>%
+ addPolylines(lng = c(morumbi_coords[1], mineirao_coords[1]), lat = c(morumbi_coords[2], mineirao_coords[2]), color = "green") %>%
+ addPolylines(lng = c(morumbi_coords[1], arena_grêmio_coords[1]), lat = c(morumbi_coords[2], arena_grêmio_coords[2]), color = "brown") %>%
+ addPolylines(lng = c(morumbi_coords[1], arena_corinthians_coords[1]), lat = c(morumbi_coords[2], arena_corinthians_coords[2]),  color = "gray") %>%
+ addPolylines(lng = c(morumbi_coords[1], arena_da_baixada_coords[1]),  lat = c(morumbi_coords[2], arena_da_baixada_coords[2]),  color = "purple") %>%
+ addPolylines(lng = c(morumbi_coords[1], castelao_coords[1]), lat = c(morumbi_coords[2], castelao_coords[2]), color = "orange") %>%
+ addPolylines(lng = c(morumbi_coords[1], beira_rio_coords[1]), lat = c(morumbi_coords[2], beira_rio_coords[2]), color = "black") %>%
+ addPolylines(lng = c(morumbi_coords[1], mane_garrincha_coords[1]), lat = c(morumbi_coords[2], mane_garrincha_coords[2]), color = "magenta") %>% 