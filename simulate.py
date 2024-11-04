
import SimulationFunctions


#print(active_product_nonprimary_list)




def whatsNext(order_list, machine_list, machine):
    """
    Finds What's Next on a machine

    #0 NonPrimary İşler ve Primary İşler ayrıldı
    #1 Beden Karışıklığı Olmasın    
    #2 İp Değiştirme Zahmeti Minumum Olsun
    #3 O anda Çalışan İşlere Yardım etsin
    #4 Yeni iş girecekse en çok bekleyeni olan işlerden birini seçsin

    """
    (active_product_primary_list, active_product_nonprimary_list) = SimulationFunctions.orderListSeperator(order_list)


    result = []

    if SimulationFunctions.isPrimary(machine):

        result.extend( sorted(SimulationFunctions.findPartDiff(machine,active_product_primary_list, machine_list), key=SimulationFunctions.totalTime, reverse=True) )
        result.extend( sorted(SimulationFunctions.findSizeDiff(machine, active_product_primary_list, machine_list), key=SimulationFunctions.totalTime, reverse=True) )
        result.extend( sorted(SimulationFunctions.findColorDiffActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findColorDiffNotActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findSameOrderActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findDiffOrderActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findSameOrderNotActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findDiffOrderNotActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )

    else:
        result.extend( sorted(SimulationFunctions.findSizeDiffSamePart(machine, active_product_nonprimary_list, machine_list), key=SimulationFunctions.totalTime, reverse=True) )
        result.extend( sorted(SimulationFunctions.findColorDiffActiveSamePart(machine, active_product_nonprimary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findColorDiffNotActiveSamePart(machine, active_product_nonprimary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findPartDiff(machine,active_product_primary_list, machine_list), key=SimulationFunctions.totalTime, reverse=True) )
        result.extend( sorted(SimulationFunctions.findSizeDiff(machine, active_product_primary_list, machine_list), key=SimulationFunctions.totalTime, reverse=True) )
        result.extend( sorted(SimulationFunctions.findColorDiffActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findColorDiffNotActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findSameOrderActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findDiffOrderActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findSameOrderNotActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )
        result.extend( sorted(SimulationFunctions.findDiffOrderNotActive(machine, active_product_primary_list, machine_list) ,key=SimulationFunctions.totalTime , reverse=True) )


    #for i in result:
        #print(i)

    return result


def printWhatsNext(order_list,  machine_list, n = SimulationFunctions.N):

    for i in range(len(machine_list)):
        print("Machine ID:", machine_list[i]["Machine"])
        result_list = whatsNext(order_list,machine_list,machine_list[i] )
        if result_list:
            for i in range(len(result_list[0:n])):
                print("Alternative",i,end="  ")
                print(result_list[i])



def workLoadDetection(machine_list, order_list):
    combinedList = SimulationFunctions.combineMachineWithOrders(machine_list, order_list)
    groupedByBantList = SimulationFunctions.groupByBant(combinedList)
    AverageMins = SimulationFunctions.averageMinByBant(groupedByBantList)
    print(AverageMins)









