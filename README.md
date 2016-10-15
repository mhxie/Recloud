# File Manager

This part the file system of our project. In this part, we try to apply the GFS(Google File System) to our system to support our distributed private cloud. However, we have made some changes to the ChunkSever part to apply our RAID part.

### Reasons for choosing the GFS
1. GFS is a file system based on inexpensive commodity.
2. The system provide fault tolerance and automatic recovery which appeal us so much.
3. It is a scalable distributed file system.

### Changes we are planning to make
we are going to change the fault tolerance with the redundant policy which more precisely is the fountain codes(喷泉吗) we will use.
The GFS uses the replicated chunks to keep fault tolerance while we are going to use erasure correcting codes(抹除码), which can keep the robustness while reduce the storage overhead.

### File interface
coming soon
