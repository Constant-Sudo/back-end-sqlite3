import { Entity, Column, PrimaryGeneratedColumn } from "typeorm"

@Entity()
export class Exams {
    @PrimaryGeneratedColumn()
    id!: number;

    @Column()
    student!: number;

    @Column()
    ratings!: [number];
}
