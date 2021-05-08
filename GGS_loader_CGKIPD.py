##### ГГС с сайта https://order.cgkipd.ru/
import json,requests
REGION_CODE=94
REGIONS_CODE=[str(i).rjust(2,'0') for i in range(1,93)]
def loadGGS_region(REGION_CODE):
    Masterlink='https://order.cgkipd.ru/api/profiles/geodesic'
    json_payload_dict={"geom":[],"name":None,"region":[REGION_CODE],"class":None,"municipal":None,"index":None}
    req=requests.post(Masterlink,json=json_payload_dict,verify=False)
    #Декодирование в json обычный
    output_response_json=req.json()
    print('Результат запроса по коду ',REGION_CODE, ' = ',req, ', количество пунктов = ', len(output_response_json))
    #Декодирование в geojson
    output_response_geojson = {'type': 'FeatureCollection','features':
                   [{'type': 'Feature','geometry' : d['geom'],'properties' : d,}
                   for d in output_response_json]
              }
    #Запись Json
    out_json_file_name='./GGS_DATA/data_cgkipd_region_'+ str(REGION_CODE)+'.json'
    with open(out_json_file_name, 'w') as output:
        json.dump(output_response_geojson, output)


def main():
    global REGION_CODE
    loadGGS_region(REGION_CODE)
    for REGION_CODE in REGIONS_CODE:
        #loadGGS_region(REGION_CODE)
        pass



if __name__ == '__main__':
    main()