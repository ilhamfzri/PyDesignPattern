import time
from npc.warrior import Warrior
from npc.mage import Mage


def main():
    ## Create 5 Mage and 5 Warrior

    ## Without Clone
    time_start = time.time()
    warrior_list = []
    mage_list = []
    for _ in range(0, 5):
        warrior = Warrior(170, 20, "Greatsword", 120)
        mage = Mage(165, 18, "Greatstaff", 90)
        
        print(f"Add warrior npc with id : {id(warrior)}")
        warrior_list.append(warrior)
        print(f"Add mage npc with id : {id(mage)}")
        mage_list.append(mage)
    processing_time = time.time() - time_start
    print(f"Processing time without clone : {int(processing_time)}")


    ## With Clone
    time_start = time.time()
    warrior_list = []
    mage_list = []
    warrior_template = Warrior(170, 20, "Greatsword", 120)
    mage_template = Mage(165, 18, "Greatstaff", 90)
    for _ in range(0, 5):
        warrior = warrior_template.clone()
        mage = mage_template.clone()
        
        print(f"Add warrior npc with id : {id(warrior)}")
        warrior_list.append(warrior)
        print(f"Add mage npc with id : {id(mage)}")
        mage_list.append(mage)
    processing_time = time.time() - time_start
    print(f"Processing time with clone : {int(processing_time)}")


if __name__ == '__main__':
    main()