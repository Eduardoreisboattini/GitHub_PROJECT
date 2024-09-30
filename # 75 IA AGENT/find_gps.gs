function calcularDistancia() {
  var planilha = SpreadsheetApp.getActiveSpreadsheet();
  var baseSheet = planilha.getSheetByName('Base');
  var consultaSheet = planilha.getSheetByName('Consulta');
  
  var baseData = baseSheet.getRange('B2:D').getValues();
  var consultaData = consultaSheet.getRange('O2:P').getValues();
  var consultaTipoData = consultaSheet.getRange('L2:L').getValues();
  var consultaInfoData = consultaSheet.getRange('I2:I').getValues();
  var consultaBData = consultaSheet.getRange('B2:B').getValues();
  
  var resultado = [];
  
  for (var i = 0; i < baseData.length; i++) {
    var baseLatitude = baseData[i][0];
    var baseLongitude = baseData[i][1];
    var baseTipo = baseData[i][2];
    
    if (baseLatitude && baseLongitude) {
      var menorDistancia = Infinity;
      var infoConsulta = '';
      var infoConsultaB = '';
      
      for (var j = 0; j < consultaData.length; j++) {
        var consultaLatitude = consultaData[j][0];
        var consultaLongitude = consultaData[j][1];
        var consultaTipo = consultaTipoData[j][0];
        
        if (consultaLatitude && consultaLongitude && consultaTipo === baseTipo) {
          var distancia = calcularDistanciaEntreCoordenadas(baseLatitude, baseLongitude, consultaLatitude, consultaLongitude);
          
          if (distancia < menorDistancia) {
            menorDistancia = distancia;
            infoConsulta = consultaInfoData[j][0];
            infoConsultaB = consultaBData[j][0];
          }
        }
      }
      
      resultado.push([menorDistancia, infoConsulta, infoConsultaB]);
    } else {
      resultado.push(['', '', '']);
    }
  }
  
  baseSheet.getRange('L2:N').setValues(resultado);
}

function calcularDistanciaEntreCoordenadas(lat1, lon1, lat2, lon2) {
  var R = 6371; // Raio da Terra em quilômetros
  var dLat = toRad(lat2 - lat1);
  var dLon = toRad(lon2 - lon1);
  var a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
    Math.sin(dLon / 2) * Math.sin(dLon / 2);
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  var distancia = R * c;
  return distancia;
}

function toRad(valor) {
  return valor * Math.PI / 180;
}

