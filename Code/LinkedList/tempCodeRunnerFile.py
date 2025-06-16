    def removeduplicate(self, head):
        map = {}
        temp = head
        while temp is not None:
            if temp.data not in map:
                map[temp.data] = 1
            temp = temp.next

        for i in map:
            print(i)