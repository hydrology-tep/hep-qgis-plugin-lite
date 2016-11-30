   �      ~http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&SERVICE=WMS&REQUEST=GetCapabilities    �����    �����         
     O K           �      Server   nginx   Content-Type   text/xml; charset=UTF-8   Vary   Accept-Encoding   Content-Encoding   gzip <?xml version='1.0' encoding="UTF-8" standalone="no" ?>
<WMS_Capabilities version="1.3.0"  xmlns="http://www.opengis.net/wms"   xmlns:sld="http://www.opengis.net/sld"   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"   xmlns:ms="http://mapserver.gis.umn.edu/mapserver"   xmlns:inspire_common="http://inspire.ec.europa.eu/schemas/common/1.0"   xmlns:inspire_vs="http://inspire.ec.europa.eu/schemas/inspire_vs/1.0"   xsi:schemaLocation="http://www.opengis.net/wms http://schemas.opengis.net/wms/1.3.0/capabilities_1_3_0.xsd  http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/sld_capabilities.xsd  http://inspire.ec.europa.eu/schemas/inspire_vs/1.0  http://inspire.ec.europa.eu/schemas/inspire_vs/1.0/inspire_vs.xsd http://mapserver.gis.umn.edu/mapserver http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;service=WMS&amp;version=1.3.0&amp;request=GetSchemaExtension">

<!-- MapServer version 6.4.1 OUTPUT=GIF OUTPUT=PNG OUTPUT=JPEG OUTPUT=KML SUPPORTS=PROJ SUPPORTS=GD SUPPORTS=AGG SUPPORTS=FREETYPE SUPPORTS=CAIRO SUPPORTS=SVG_SYMBOLS SUPPORTS=RSVG SUPPORTS=ICONV SUPPORTS=FRIBIDI SUPPORTS=WMS_SERVER SUPPORTS=WMS_CLIENT SUPPORTS=WFS_SERVER SUPPORTS=WFS_CLIENT SUPPORTS=WCS_SERVER SUPPORTS=SOS_SERVER SUPPORTS=FASTCGI SUPPORTS=THREADS SUPPORTS=GEOS INPUT=JPEG INPUT=POSTGIS INPUT=OGR INPUT=GDAL INPUT=SHAPEFILE -->

<Service>
  <Name>WMS</Name>
  <Title>ECMWF_ATP_160_SST</Title>
  <Abstract>Mapas de previsão tri-horária da temperatura à superfície do mar em Kelvin para a região do Atlântico, gerado pelo ECMWF, para as próximas 120 horas.</Abstract>
  <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/>
  <ContactInformation>
    <ContactPersonPrimary>
      <ContactPerson>Divisão de Sistemas de Informação, Comunicações e Desenvolvimento Tecnológico (DivSI)</ContactPerson>
      <ContactOrganization>Instituto Português do Mar e da Atmosfera (IPMA)</ContactOrganization>
    </ContactPersonPrimary>
  <ContactElectronicMailAddress>webmaster@ipma.pt</ContactElectronicMailAddress>
  </ContactInformation>
  <MaxWidth>2048</MaxWidth>
  <MaxHeight>2048</MaxHeight>
</Service>

<Capability>
  <Request>
    <GetCapabilities>
      <Format>text/xml</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Post>
        </HTTP>
      </DCPType>
    </GetCapabilities>
    <GetMap>
      <Format>image/png</Format>
      <Format>image/jpeg</Format>
      <Format>image/gif</Format>
      <Format>image/png; mode=8bit</Format>
      <Format>application/x-pdf</Format>
      <Format>image/svg+xml</Format>
      <Format>image/tiff</Format>
      <Format>application/vnd.google-earth.kml+xml</Format>
      <Format>application/vnd.google-earth.kmz</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Post>
        </HTTP>
      </DCPType>
    </GetMap>
    <GetFeatureInfo>
      <Format>text/html</Format>
      <Format>application/vnd.ogc.gml</Format>
      <Format>text/plain</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Post>
        </HTTP>
      </DCPType>
    </GetFeatureInfo>
    <sld:DescribeLayer>
      <Format>text/xml</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Post>
        </HTTP>
      </DCPType>
    </sld:DescribeLayer>
    <sld:GetLegendGraphic>
      <Format>image/png</Format>
      <Format>image/jpeg</Format>
      <Format>image/gif</Format>
      <Format>image/png; mode=8bit</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Post>
        </HTTP>
      </DCPType>
    </sld:GetLegendGraphic>
    <ms:GetStyles>
      <Format>text/xml</Format>
      <DCPType>
        <HTTP>
          <Get><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Get>
          <Post><OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;"/></Post>
        </HTTP>
      </DCPType>
    </ms:GetStyles>
  </Request>
  <Exception>
    <Format>XML</Format>
    <Format>INIMAGE</Format>
    <Format>BLANK</Format>
  </Exception>
  <sld:UserDefinedSymbolization SupportSLD="1" UserLayer="0" UserStyle="1" RemoteWFS="0" InlineFeature="0" RemoteWCS="0"/>
  <inspire_vs:ExtendedCapabilities>
    <inspire_common:MetadataUrl xsi:type="inspire_common:resourceLocatorType">
      <inspire_common:URL>http://maps.ipma.pt/metadata/forecasts/oceanography/ecmwf_atp_160_sst__srv.xml</inspire_common:URL>
      <inspire_common:MediaType>application/vnd.ogc.csw.capabilities.response_xml</inspire_common:MediaType>
    </inspire_common:MetadataUrl>
    <inspire_common:SupportedLanguages>
      <inspire_common:DefaultLanguage><inspire_common:Language>por</inspire_common:Language></inspire_common:DefaultLanguage>
      <inspire_common:SupportedLanguage><inspire_common:Language>eng</inspire_common:Language></inspire_common:SupportedLanguage>
    </inspire_common:SupportedLanguages>
    <inspire_common:ResponseLanguage><inspire_common:Language>por</inspire_common:Language></inspire_common:ResponseLanguage>
  </inspire_vs:ExtendedCapabilities>
  <Layer>
    <Name>ecmwf_atp_160_sst</Name>
    <Title>ECMWF_ATP_160_SST</Title>
    <Abstract>Mapas de previsão tri-horária da temperatura à superfície do mar em Kelvin para a região do Atlântico, gerado pelo ECMWF, para as próximas 120 horas.</Abstract>
    <CRS>EPSG:3857</CRS>
    <EX_GeographicBoundingBox>
        <westBoundLongitude>-0.000332938</westBoundLongitude>
        <eastBoundLongitude>5.61447e-07</eastBoundLongitude>
        <southBoundLatitude>0.000250967</southBoundLatitude>
        <northBoundLatitude>0.000419401</northBoundLatitude>
    </EX_GeographicBoundingBox>
    <BoundingBox CRS="EPSG:3857"
                minx="-37.0625" miny="27.9375" maxx="0.0625" maxy="46.6875" />
    <Style>
       <Name>default</Name>
       <Title>default</Title>
       <LegendURL width="77" height="11813">
          <Format>image/png</Format>
          <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst&amp;format=image/png&amp;STYLE=default"/>
       </LegendURL>
    </Style>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_000</Name>
        <Title>ecmwf_atp_160_sst_000</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 00 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_000&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_003</Name>
        <Title>ecmwf_atp_160_sst_003</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 03 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_003&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_006</Name>
        <Title>ecmwf_atp_160_sst_006</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 06 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_006&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_009</Name>
        <Title>ecmwf_atp_160_sst_009</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 09 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_009&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_012</Name>
        <Title>ecmwf_atp_160_sst_012</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 12 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_012&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_015</Name>
        <Title>ecmwf_atp_160_sst_015</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 15 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_015&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_018</Name>
        <Title>ecmwf_atp_160_sst_018</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 18 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_018&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_021</Name>
        <Title>ecmwf_atp_160_sst_021</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 21 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_021&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_024</Name>
        <Title>ecmwf_atp_160_sst_024</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 24 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_024&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_027</Name>
        <Title>ecmwf_atp_160_sst_027</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 27 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_027&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_030</Name>
        <Title>ecmwf_atp_160_sst_030</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 30 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_030&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_033</Name>
        <Title>ecmwf_atp_160_sst_033</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 33 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_033&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_036</Name>
        <Title>ecmwf_atp_160_sst_036</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 36 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_036&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_039</Name>
        <Title>ecmwf_atp_160_sst_039</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 39 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_039&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_042</Name>
        <Title>ecmwf_atp_160_sst_042</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 42 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_042&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_045</Name>
        <Title>ecmwf_atp_160_sst_045</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 45 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_045&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_048</Name>
        <Title>ecmwf_atp_160_sst_048</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 48 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_048&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_051</Name>
        <Title>ecmwf_atp_160_sst_051</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 51 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_051&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_054</Name>
        <Title>ecmwf_atp_160_sst_054</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 54 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_054&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_057</Name>
        <Title>ecmwf_atp_160_sst_057</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 57 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_057&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_060</Name>
        <Title>ecmwf_atp_160_sst_060</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 60 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_060&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_063</Name>
        <Title>ecmwf_atp_160_sst_063</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 63 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_063&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_066</Name>
        <Title>ecmwf_atp_160_sst_066</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 66 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_066&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_069</Name>
        <Title>ecmwf_atp_160_sst_069</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 69 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_069&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_072</Name>
        <Title>ecmwf_atp_160_sst_072</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 72 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_072&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_075</Name>
        <Title>ecmwf_atp_160_sst_075</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 75 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_075&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_078</Name>
        <Title>ecmwf_atp_160_sst_078</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 78 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_078&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_081</Name>
        <Title>ecmwf_atp_160_sst_081</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 81 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_081&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_084</Name>
        <Title>ecmwf_atp_160_sst_084</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 84 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_084&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_087</Name>
        <Title>ecmwf_atp_160_sst_087</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 87 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_087&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_090</Name>
        <Title>ecmwf_atp_160_sst_090</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 90 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_090&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_093</Name>
        <Title>ecmwf_atp_160_sst_093</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 93 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_093&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_096</Name>
        <Title>ecmwf_atp_160_sst_096</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 96 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_096&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_099</Name>
        <Title>ecmwf_atp_160_sst_099</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 99 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_099&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_102</Name>
        <Title>ecmwf_atp_160_sst_102</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 102 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_102&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_105</Name>
        <Title>ecmwf_atp_160_sst_105</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 105 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_105&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_108</Name>
        <Title>ecmwf_atp_160_sst_108</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 108 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_108&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_111</Name>
        <Title>ecmwf_atp_160_sst_111</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 111 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_111&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_114</Name>
        <Title>ecmwf_atp_160_sst_114</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 114 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_114&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_117</Name>
        <Title>ecmwf_atp_160_sst_117</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 117 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_117&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
    <Layer queryable="1" opaque="0" cascaded="0">
        <Name>ecmwf_atp_160_sst_120</Name>
        <Title>ecmwf_atp_160_sst_120</Title>
        <Abstract>ECMWF SST - Temperatura à Superfície do Mar - Hora 120 UTC</Abstract>
        <CRS>EPSG:4326</CRS>
        <EX_GeographicBoundingBox>
            <westBoundLongitude>-37.0625</westBoundLongitude>
            <eastBoundLongitude>0.0625</eastBoundLongitude>
            <southBoundLatitude>27.9375</southBoundLatitude>
            <northBoundLatitude>46.6875</northBoundLatitude>
        </EX_GeographicBoundingBox>
        <BoundingBox CRS="EPSG:4326"
                    minx="27.9375" miny="-37.0625" maxx="46.6875" maxy="0.0625" />
        <Style>
          <Name>default</Name>
          <Title>default</Title>
          <LegendURL width="77" height="293">
             <Format>image/png</Format>
             <OnlineResource xmlns:xlink="http://www.w3.org/1999/xlink" xlink:type="simple" xlink:href="http://maps.ipma.pt/mapserv?map=/var/www/maps/forecasts/oceanography/ecmwf_atp_160_sst.map&amp;language=por&amp;version=1.3.0&amp;service=WMS&amp;request=GetLegendGraphic&amp;sld_version=1.1.0&amp;layer=ecmwf_atp_160_sst_120&amp;format=image/png&amp;STYLE=default"/>
          </LegendURL>
        </Style>
    </Layer>
  </Layer>
</Capability>
</WMS_Capabilities>
